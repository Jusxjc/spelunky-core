import pygame
from maps import test_map
from tilemap import *
from settings import *
from player import Player

# Load map data
map_data = test_map.MAP
tiles: tile_map = tile_map(map_data, t_size)

# Initialize Pygame
pygame.init()

# Clock to set tick speed to 60 FPS
clock = pygame.time.Clock()
delta_time = 0.1

# Create player
player = Player(256, 256, tiles)

# Create window
screen = pygame.display.set_mode((screen_x, screen_y))

running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Tick 60 FPS
    delta_time = clock.tick(60) / 1000
    delta_time = max(0.001, min(0.1, delta_time))

    # Update game logic
    player.update(pygame.key.get_pressed())

    # Draw tilemap and player
    tiles.draw_tilemap(screen)
    player.draw(screen)

    # Update display
    pygame.display.flip()

pygame.quit()