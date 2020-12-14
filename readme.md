
This readme will continously document the game's development.

# List of overall goals
1. Make players and entities spawn on the map
2. Implement FOV in the game.
3. Update the UML class model


# Current goal
1. Make player and entities spawn on the map

# Required parts for current goal
1. Generic entities
2. Ability to generate a map
3. Spawn functionality

# Continuously updated list of steps  
1. Create functionality to spawn entities during map generation.
    - Create spawn entity function within the entity
2. Set the player's spawn position in the first created room in the dungeon.
3. Create a list in map_generation which gets filled according to an input number of max enemies
4. Use the entity spawn function to set each entity's spawn location x and y
5. Render each entity by calling the gameMap render function from the engine.

# Finished steps
1. The actual game map file and class
2. The tiles to be used within the game map class

# Completed goals
1. Get a character to move inside of the game's console.
2. Establish the game's engine.
3. Implement the actual game map and make a character move on it
4. Implement the procedural map generator
5. Refactor the code and change casing to underscores






