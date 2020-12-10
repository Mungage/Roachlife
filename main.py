#!/usr/bin/env python3

# Purpose of the 

import tcod

def main() -> None:
    """The main function loads all the required variables, instantiates the tcod console, tcod context and the game engine. 
    It then continuously executes the game loop by calling the engine"""
    
    consoleWidth = 80
    consoleHeight = 60
    title = "Roachlife"

    tileset = tcod.tileset.load_tilesheet("dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_CP437)
    console = tcod.Console(consoleWidth, consoleHeight)

    # The tcod context 
    with tcod.context.new(width=consoleWidth, height=consoleHeight, tileset= tileset, title = title, vsync = True) as context:
        while True:
            console.clear()
            console.print(x=0, y=0, string="@")
            context.present(console)

            for event in tcod.event.wait():
                context.convert_event(event)
                print(event)
                if event.type == "QUIT":
                    raise SystemExit()

if __name__ == "__main__":
    main()