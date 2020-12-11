class Action:
    """The purpose of the Action class is to perform all the actions that occur within the game loop"""
    pass

class EscapeAction(Action):
    pass

class MovementAction(Action):
    """The movementAction class contains the functions required for entities to perform movements inside of the game.
    In order to move the entities on the tilemap made of an x and and y plane. All the game's movements need to occur within this plane.
    """

    def __init__(self, xDirection: int, yDirection: int):
        # super() is a function that returns the proxy object, i.e. the inheriting object. 
        # This function allows you to gain access to inherited methods from sibling or parent class.
        super().__init__()    
        
        self.xDirection = xDirection
        self.yDirection = yDirection

