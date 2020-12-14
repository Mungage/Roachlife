from __future__ import annotations  # Does something with the way the code is interpreted, solved a NameError

import random
from typing import Iterator, List, Tuple, TYPE_CHECKING

import tcod

from gameMap import GameMap
import tileTypes

import definedEntities

if TYPE_CHECKING:
    from entity import Entity

class Room:
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x1 = x
        self.y1 = y
        self.x2 = x + width
        self.y2 = y + height

    # We want to decide the room's area, which is defined as a 2D array i.e. the two slices x1:x2 and y1:y2
    @property
    def determine_room_center(self) -> Tuple[int, int]:
        # We want to get the center coordinate of the room
        # We do this by dividing the full room by 2, we need to return a coordinate x and y.
        # This can be done as a Tuple I presume.
        center_x = int((self.x1 + self.x2) / 2)
        center_y = int((self.y1 + self.y2) / 2)
        
        return center_x, center_y
    
    @property
    def determine_room_size(self) -> Tuple[slice, slice]:
        return slice(self.x1 + 1, self.x2 + 1), slice(self.y1 + 1, self.y2)

    def check_room_collisions(self, other_room: Room) -> bool:
        # if rooms outer x1, x2 and y1, y2 intersects with another room, return true
        return (self.x1 <= other_room.x2 and self.x2 >= other_room.x1 and self.y1 <= other_room.y2 and self.y2 >= other_room.y1)

def generate_connections(start: Tuple[int, int], end: Tuple[int, int]) -> Iterator[Tuple[int, int]]:
    # We want to establish a connection between each of the generated rooms, the tutorial does it with tcod.los.bresenham algorithm
    # It does it by specifying two endpoints, a start and an end, with a Tuple each.
    # the Tuples represent the coordinates for said ending and starting points.
    # The function returns an L-shaped tunnel between these two points.
    # it uses a random function to decide when the tunnel moves horizontally and then vertically.
    # It does this with an if... else statement
    # It then generates the coordinates for the tunnel with the Bresenham function.
    # The bresenham function takes an x and y coordinate, and the corner x and y coordinates and puts them to a list. and then
    # uses yield to return a x and y as generators.

    x1, y1 = start
    x2, y2 = end
    if random.random() < 0.5:
        corner_x, corner_y = x2, y1
    else:
        corner_x, corner_y = x1, y2

    for x, y in tcod.los.bresenham((x1, y1), (corner_x, corner_y)).tolist():
        yield x, y      # Yield returns a Generator, which are an interesting part of python. They essentially mean that the function can continue to pick up where it left
                        # off when called again. Instead of starting from the beginning. 
                        # This is useful because we will interate the x and y values that we receive from the function to dig the tunnel
    for x, y in tcod.los.bresenham((corner_x, corner_y), (x2, y2)).tolist():
        yield x, y

def spawn_entities(room: Room, game_map: GameMap, maximum_monsters: int) -> None:
    number_of_monsters = random.randint(0, maximum_monsters)

    for i in range(number_of_monsters):
        x = random.randint(room.x1 + 1, room.x2 -1)
        y = random.randint(room.y1 + 1, room.y2 - 1)

        if not any(entity.x == x and entity.y == y for entity in game_map.entities):
            definedEntities.enemy.spawn(game_map, x, y)

def generate_game_map(map_width: int, map_height: int, max_rooms: int, min_room_size: int, max_room_size: int, max_enemies_per_room: int, player: Entity) -> GameMap:
    game_map = GameMap(map_width, map_height, entities=[player])
    
    rooms: List[Room] = []

    for r in range(max_rooms):
        # Pick the x and y size for the room
        room_x_width = random.randint(min_room_size, max_room_size)   
        room_y_height = random.randint(min_room_size, max_room_size)
       # Pick the coordinates to place the room
        x = random.randint(0, game_map.width - room_x_width - 1)
        y = random.randint(0, game_map.height - room_y_height - 1)
        # Add a new instance with the randomized integers
        new_room = Room(x, y, room_x_width, room_y_height)

        # We want to check whether the list rooms has rooms that overlap with the new room before adding it to the list.
        # We do this by checking the new room against every room in the list. This requires a loop

        if any(new_room.check_room_collisions(other_room) for other_room in rooms):
            continue

        game_map.tiles[new_room.determine_room_size] = tileTypes.floor

        try:
            if len(rooms) == 0:
                player.x, player.y = new_room.determine_room_center
                game_map.entities.append(player)
            else:
                for x, y in generate_connections(rooms[-1].determine_room_center, new_room.determine_room_center):
                    game_map.tiles[x, y] = tileTypes.floor
        except:
            print("An exception occurred when trying to generate rooms on the game map")
        
        spawn_entities(new_room, game_map, max_enemies_per_room)

        rooms.append(new_room)

    # For each room
    # while max enemies > 0
    # Add random amount of enemies between 0 and 3 : while random amount of enemies > 0 -> add 1 new enemy to list
    # 


    # for each room in list of rooms -> spawn enemies of a certain type.
    # If max enemies > 0.
    # pick a random set of coordinates inside a room x, y
    # Spawn new entity and set its coordinates to said x, y coordinates.

    # We've got the rooms generated in the loop and appended to the list.
    # If room x overlaps with room y in list of rooms. Repeat the loop
    return game_map



