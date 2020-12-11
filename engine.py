
# The purpose of this file is to hold the game engine class. The game engine object is the one that gets continuously called in the game loop,
# holding reference to the other objects and continously calling the appropriate functions. In other words the game engine is the point from where
# Everything in the game gets run.

from typing import Set, Iterable, Any

import tcod.event

from tcod.console import Console
from tcod.context import Context

from eventHandler import EventHandler
from entity import Entity
from gameMap import GameMap

class Engine:
    """The game engine is the object that continously executes the appropriate functions required for progressing the game loop forward
    It does this by holding reference to all the main components """

    gameMap: GameMap
    
    def __init__(self, entities: Set[Entity], eventHandler: EventHandler, gameMap: GameMap, player: Entity) -> None:
        self.eventHandler = eventHandler
        self.gameMap = gameMap
        self.entities = entities
        self.player = player

    def handleEvents(self, events: Iterable[Any]) -> None:
        """The gateway function which handles all the game loop related events in the game"""
        for event in events:
            action = self.eventHandler.dispatch(event)

            if action is None:
                continue

            if self.gameMap.tiles["walkable"][self.player.x + action.dx, self.player.y + action.dy]:
                self.player.moveEntity(dx=action.dx, dy=action.dy)

    def render(self, console: Console, context: Context) -> None:
        """The render function renders the tcod console and tcod context for us.
        by doing this it can display all the entities and respond to actions for us.
        The rendering function is run each game loop to update what is displayed to the user
        """
        
        self.gameMap.renderMap(console)

        for entity in self.entities:
            console.print(entity.x, entity.y, entity.charTile, fg=entity.color)

        context.present(console)
        console.clear()





    






