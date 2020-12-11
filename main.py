#!/usr/bin/env python3
import copy
import tcod
import traceback

from typing import Iterable, Set

from actions import Action, EscapeAction, MovementAction 
from eventHandler import EventHandler
from engine import Engine
from entity import Entity
from gameMap import GameMap

def main() -> None:
    """The main function loads all the required variables, instantiates the tcod console, tcod context and the game engine. 
    It then continuously executes the game loop by calling the engine"""
    
    title = "Roachlife"
    consoleWidth = 120
    consoleHeight = 80

    mapWidth = 120
    mapHeight = 75
   
    tileset = tcod.tileset.load_tilesheet("dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD)

    player = Entity(int(consoleWidth / 2), int(consoleHeight / 2), "@", [255, 255, 255]) 
    entities = {player}
    
    gameMap = GameMap(mapWidth, mapHeight)
    eventHandler = EventHandler()               # We initialize the eventHandler object to be inputted into the engine.

    engine = Engine(entities = entities, eventHandler = eventHandler, gameMap = gameMap, player = player)       # We initialize the engine with the EventHandler object and a player object representing the player character.
    
    # The tcod context 
    with tcod.context.new_terminal(consoleWidth, consoleHeight, tileset= tileset, title = title, vsync = True) as context:
        
        console = tcod.Console(consoleWidth, consoleHeight, order="F")
         
        while True:
            try:
                engine.render(console, context)
                
                events = tcod.event.wait()

                engine.handleEvents(events)
            except Exception:
                traceback.print_exc()

if __name__ == "__main__":
    main()