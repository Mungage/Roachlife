#!/usr/bin/env python3
import copy
import tcod
import traceback

import definedEntities

from typing import Iterable, Set

from actions import EscapeAction, MovementAction 
from eventHandler import EventHandler
from engine import Engine
from entity import Entity

def main() -> None:
    """The main function loads all the required variables, instantiates the tcod console, tcod context and the game engine. 
    It then continuously executes the game loop by calling the engine"""
    
    title = "Roachlife"
    consoleWidth = 120
    consoleHeight = 80
    tileset = tcod.tileset.load_tilesheet("dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD)

    player = copy.deepcopy(definedEntities.player)
    listOfEntities = {player}
    eventHandler = EventHandler()
    engine = Engine(eventHandler, player, listOfEntities)
    console = tcod.Console(consoleWidth, consoleHeight, order="F")

    # The tcod context 
    with tcod.context.new_terminal(consoleWidth, consoleHeight, tileset= tileset, title = title, vsync = True) as context:

        while True:
            try:
                events = tcod.event.wait()
                engine.handleEvents(events)
                engine.render(console, context)
            except Exception:
                traceback.print_exc()

if __name__ == "__main__":
    main()