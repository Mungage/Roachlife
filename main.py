#!/usr/bin/env python3
import copy
import tcod
import traceback

from engine import Engine
from entity import Entity
from gameMap import GameMap
from eventHandler import EventHandler
from mapGenerator import generate_game_map

def main() -> None:
    """The main function loads all the required variables, instantiates the tcod console, tcod context and the game engine. 
    It then continuously executes the game loop by calling the engine"""
    
    title = "Roachlife"
    console_width = 80
    console_height = 50

    map_width = 80
    map_height = 45

    max_room_size = 10
    min_room_size = 5
    max_rooms = 20

    tileset = tcod.tileset.load_tilesheet("dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD)
    
    ### Instantiating the objects to use for testing ### 
    player = Entity(int(console_width / 2), int(console_height / 2), "@", (255, 255, 255))
    entities = {player}
    
    ### Instantiating the objects to use for testing ###
    game_map = generate_game_map(  
        map_width = map_width,
        map_height = map_height,
        max_rooms = max_rooms,
        min_room_size = min_room_size,
        max_room_size = max_room_size,
        player = player
    )

    event_handler = EventHandler()   # We initialize the eventHandler object to be inputted into the engine.
    engine = Engine(event_handler = event_handler, game_map = game_map, player = player)       # We initialize the engine with the EventHandler object and a player object representing the player character.
    
    # The tcod context 
    with tcod.context.new_terminal(console_width, console_height, tileset= tileset, title = title, vsync = True) as context:

        console = tcod.Console(console_width, console_height, order="F")
        while True:
            engine.render(console, context)
            events = tcod.event.wait()
            engine.handle_events(events)

        
if __name__ == "__main__":
    main()