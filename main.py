#!/usr/bin/env python3

import tcod

from actions import EscapeAction, MovementAction 
from eventHandler import EventHandler
from engine import Engine
from player import Player

def main() -> None:
    """The main function loads all the required variables, instantiates the tcod console, tcod context and the game engine. 
    It then continuously executes the game loop by calling the engine"""
    
    consoleWidth = 80
    consoleHeight = 50
    title = "Roachlife"
    tileset = tcod.tileset.load_tilesheet("dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD)

    player = Player(int(consoleWidth / 2), int(consoleHeight / 2), "@")
    eventHandler = EventHandler()
    engine = Engine(eventHandler, player)
    console = tcod.Console(consoleWidth, consoleHeight, order="F")

    # The tcod context 
    with tcod.context.new_terminal(consoleWidth, consoleHeight, tileset= tileset, title = title, vsync = True) as context:

        while True:
            events = tcod.event.wait()
            engine.handleEvents(events)
            engine.render(console, context)

if __name__ == "__main__":
    main()