import pygame

class tile_map:
    def __init__(self,map_array,tile_size):
        self.map_array =map_array
        self.tile_size=tile_size

    def draw_tilemap(self,screen):
        tile_dic= {
            0: (18, 18, 18),      # empty / air → very dark charcoal
            1: (110, 90, 60),     # wall → earthy brown stone
            2: (150, 120, 80),   # platform → lighter sandstone
        }
        #Indexes through an array and draws a rectangle (tile)
        for row in range(len(self.map_array)):
            for column in range(len(self.map_array[row])):
                pygame.draw.rect(screen,tile_dic[self.map_array[row][column]],#Screen to draw tile and it's color
                                 ((self.tile_size*column),(self.tile_size*row),# Tile location
                                  self.tile_size,self.tile_size))# Tile size