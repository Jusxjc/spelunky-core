import pygame
from settings import *
from tilemap import tile_map

class Player:
    def __init__(self, x,y,my_map):
        self.x=x
        self.y=y
        self.speed= 4
        self.rect= pygame.Rect(x,y,p_size,p_size)
        self.falling= True
        self.jumping= True
        self.my_map=my_map
        self.y_velocity= gravity

    def draw(self, screen):
        pygame.draw.rect(screen,"blue", self.rect)

    def move_x(self, key):
    # move left
        if key[pygame.K_a] or key[pygame.K_LEFT]:
            next_left = self.rect.left - self.speed
            top = self.rect.top
            bottom = self.rect.bottom - 1
            if self.my_map.is_solid(next_left // t_size, top // t_size) or \
            self.my_map.is_solid(next_left // t_size, bottom // t_size):
                self.rect.left = ((next_left // t_size) + 1) * t_size
            else:
                self.rect.x -= self.speed

        # move right
        if key[pygame.K_d] or key[pygame.K_RIGHT]:
            next_right = self.rect.right + self.speed
            top = self.rect.top
            bottom = self.rect.bottom - 1
            if self.my_map.is_solid(next_right // t_size, top // t_size) or \
            self.my_map.is_solid(next_right // t_size, bottom // t_size):
                self.rect.right = (next_right // t_size) * t_size
            else:
                self.rect.x += self.speed
    
    def move_y(self, key):
        # jump if grounded
        if (key[pygame.K_SPACE] or key[pygame.K_UP]) and \
        self.my_map.is_solid(self.rect.centerx // t_size, (self.rect.bottom + 1) // t_size):
            self.y_velocity = -jump_height

        # apply gravity
        self.y_velocity += gravity

        if self.y_velocity > 0:  # falling
            next_bottom = self.rect.bottom + self.y_velocity
            if self.my_map.is_solid(self.rect.centerx // t_size, next_bottom // t_size):
                tile_y = next_bottom // t_size
                self.rect.bottom = tile_y * t_size
                self.y_velocity = 0
            else:
                self.rect.y += self.y_velocity

        elif self.y_velocity < 0:  # jumping
            next_top = self.rect.top + self.y_velocity
            if self.my_map.is_solid(self.rect.centerx // t_size, next_top // t_size):
                tile_y = next_top // t_size
                self.rect.top = (tile_y + 1) * t_size
                self.y_velocity = 0
            else:
                self.rect.y += self.y_velocity       

    def update(self,key):
        self.move_x(key)
        self.move_y(key)

