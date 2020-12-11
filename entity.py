
from typing import Tuple

class Entity:
    """The generic entity class. Almost everything that is interactable in the game is an entity.
    The entities are defined within the definedEntities class
    """
    
    def __init__(self, x: int, y: int, charTile: str, color: Tuple[int, int, int]):
        self.x = x
        self.y = y
        self.charTile = charTile
        self.color = color

    def moveEntity(self, dx: int, dy: int) -> None:
        self.x += dx
        self.y += dy



