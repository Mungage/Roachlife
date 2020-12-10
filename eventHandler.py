# The eventhandler handles all the events in the game.

import tcod.event

from actions import Action, EscapeAction, MovementAction

MOVE_KEYS = {  # key_symbol: (x, y)
        # Arrow keys.
        tcod.event.K_LEFT: (-1, 0),
        tcod.event.K_RIGHT: (1, 0),
        tcod.event.K_UP: (0, -1),
        tcod.event.K_DOWN: (0, 1),
        tcod.event.K_HOME: (-1, -1),
        tcod.event.K_END: (-1, 1),
        tcod.event.K_PAGEUP: (1, -1),
        tcod.event.K_PAGEDOWN: (1, 1),
        tcod.event.K_PERIOD: (0, 0),
        # Numpad keys.
        tcod.event.K_KP_1: (-1, 1),
        tcod.event.K_KP_2: (0, 1),
        tcod.event.K_KP_3: (1, 1),
        tcod.event.K_KP_4: (-1, 0),
        tcod.event.K_KP_5: (0, 0),
        tcod.event.K_KP_6: (1, 0),
        tcod.event.K_KP_7: (-1, -1),
        tcod.event.K_KP_8: (0, -1),
        tcod.event.K_KP_9: (1, -1),
        tcod.event.K_CLEAR: (0, 0),  # Numpad `clear` key.
        # Vi Keys.
        tcod.event.K_h: (-1, 0),
        tcod.event.K_j: (0, 1),
        tcod.event.K_k: (0, -1),
        tcod.event.K_l: (1, 0),
        tcod.event.K_y: (-1, -1),
        tcod.event.K_u: (1, -1),
        tcod.event.K_b: (-1, 1),
        tcod.event.K_n: (1, 1),
    }

class EventHandler(tcod.event.EventDispatch[Action]):
    
    def ev_quit(self, event:tcod.event.Quit) -> None:
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> None:
        action = None
        key = event.sym

        if key == tcod.event.K_UP:
            action = MovementAction(directionX=0, directionY=-1)
        elif key == tcod.event.K_DOWN:
            action = MovementAction(directionX=0, directionY=1)
        elif key == tcod.event.K_RIGHT:
            action = MovementAction(directionX=1, directionY=0)
        elif key == tcod.event.K_LEFT:
            action = MovementAction(directionX=-1,directionY=0)

        elif key == tcod.event.K_ESCAPE:
            action = EscapeAction

        return action



        




