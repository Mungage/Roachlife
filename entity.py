from __future__ import annotations

import copy

from typing import Tuple, TypeVar, TYPE_CHECKING

if TYPE_CHECKING:
    from gameMap import GameMap

T = TypeVar("T", bound="Entity")

class Entity:
    """The generic entity class. Almost everything that is interactable in the game is an entity.
    The entities are defined within the definedEntities class
    """
    def __init__(self, x: int = 0, y: int = 0, charTile: str = "?", color: Tuple[int, int, int] = (255, 255, 255), name: str = "<Undefined>", blocks_movement: bool = False,):
        self.x = x
        self.y = y
        self.charTile = charTile
        self.color = color
        self.name = name
        self.blocks_movement = blocks_movement

    def spawn(self: T, game_map: GameMap, x: int, y: int) -> T:
        clone = copy.deepcopy(self)
        clone.x = x
        clone.y = y
        game_map.entities.add(clone)
        return clone

    def move_entity(self, dx: int, dy: int) -> None:
        self.x += dx
        self.y += dy

# We need the ability to spawn an entity during the procedural map generation.
# 1. Create spawn entity function(self, x, y, )
# 2. 
#.3. 
# 4.



    
