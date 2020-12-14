from entity import Entity

player = Entity(charTile = "@", color = [255, 255, 255], name="Player", blocks_movement=True)

enemy = Entity(charTile = "E", color = [255, 255, 0], name="Enemy", blocks_movement=True)