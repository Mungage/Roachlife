from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine import Engine
    from entity import Entity

class Action:
    """The purpose of the Action class is to perform all the actions that occur within the game loop"""
    def perform(self, engine: Engine, entity: Entity) -> None:
        raise NotImplementedError

class EscapeAction(Action):
    def perform(self, engine: Engine, entity: Entity) -> None:
        raise SystemExit()

class MovementAction(Action):
    """The movementAction class contains the functions required for entities to perform movements inside of the game.
    In order to move the entities on the tilemap made of an x and and y plane. All the game's movements need to occur within this plane.
    """
    def __init__(self, dx: int, dy: int):
        # super() is a function that returns the proxy object, i.e. the inheriting object. 
        # This function allows you to gain access to inherited methods from sibling or parent class.
        super().__init__()    
        
        self.dx = dx
        self.dy = dy

    # The perform method 
    def perform(self, engine: Engine, entity: Entity) -> None:
        destX = entity.x + self.dx
        destY = entity.y + self.dy

        if not engine.game_map.inside_boudaries(destX, destY):
            return
        if not engine.game_map.tiles["walkable"][destX, destY]:
            return

        entity.move_entity(self.dx, self.dy)