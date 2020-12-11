

class Entity:
    """The generic entity class. Almost everything that is interactable in the game is an entity.
    The entities are defined within the definedEntities class
    """
    def __init__(self, x: int = 0, y: int = 0, tile: str = "?", entityType: str = "<Undefined>", name: str = "<Undefined>"):
        self.x = x
        self.y = y
        self.characterTile = tile
        self.entityType = entityType
        self.characterName = name

    def moveEntity(self, xDirection: int, yDirection: int):
        self.x = xDirection
        self.y = yDirection

class Actor(Entity):
    def __init__(self, *, x: int, y: int, tile: str = "?", entityType: str = "<Undefined>", name: str = "<Undefined>"):
        super().__init__(x = x, y = y, tile = tile, entityType = entityType, name = name)




