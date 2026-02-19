import pygame
from maps import test_map
from tilemap import *
from settings import *
map_data =test_map.MAP
tiles: tile_map = tile_map(map_data,t_size)

pygame.init()
#Test map runs to get map data


screen = pygame.display.set_mode((screen_x,screen_y)) #Creates pygame window
tiles.draw_tilemap(screen)
running = True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running= False
    pygame.display.flip()
        

pygame.quit()
