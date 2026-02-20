import pygame

class tile_map:
    def __init__(self, map_array, tile_size):
        self.map_array = map_array
        self.tile_size = tile_size

    def draw_tilemap(self, screen):
        # Tile color dictionary
        tile_dic = {
            0: (18, 18, 18),     # empty / air = very dark charcoal
            1: (110, 90, 60),    # wall = earthy brown stone
            2: (150, 120, 80),   # platform = lighter sandstone
        }

        # Loop through map array and draw tiles
        for row in range(len(self.map_array)):
            for column in range(len(self.map_array[row])):
                color = tile_dic[self.map_array[row][column]]
                rect = (self.tile_size * column, 
                        self.tile_size * row, 
                        self.tile_size, 
                        self.tile_size)
                pygame.draw.rect(screen, color, rect)

    def is_solid(self, tile_x, tile_y):
        #Return True if the tile is solid, False if air.
        tile = self.map_array[tile_y][tile_x]
        if tile == 0:  # air
            return False
        elif tile == 1:  # wall
            return True
        elif tile == 2:  # platform
            return True