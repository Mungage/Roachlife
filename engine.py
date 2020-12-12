
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
    
    def __init__(self, eventHandler: EventHandler, gameMap: GameMap, player: Entity) -> None:
        self.event_handler = eventHandler
        self.game_map = gameMap
        self.player = player

    def handle_events(self, events: Iterable[Any]) -> None:
        """The gateway function which handles all the game loop related events in the game"""
        for event in events:
            action = self.event_handler.dispatch(event)

            if action is None:
                continue

            action.perform(self, self.player)   # We insert the engine object itself, and the player entity upong which we perform the actions.

    def render(self, console: Console, context: Context) -> None:
        """The render function renders the tcod console and tcod context for us.
        by doing this it can display all the entities and respond to actions for us.
        The rendering function is run each game loop to update what is displayed to the user
        """
        # Shall call the game renderer object to render the different elements of the game, including the game map, the entities and the console.
        
        self.game_map.render_map(console)

        context.present(console)
        console.clear()





    






