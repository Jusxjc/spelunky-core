import pygame
from settings import *
from tilemap import tile_map

class Player:
    def __init__(self, x,y,my_map):
        self.x=x
        self.y=y
        self.speed= 4
        self.rect= pygame.Rect(x,y,p_size,p_size)
        self.image = pygame.image.load("assets/tiles/sprites/hero_16x16_idle_south1.png").convert_alpha()
        self.falling= True
        self.jumping= True
        self.my_map=my_map
        self.y_velocity= gravity
        self.direction= "right"
        self.idle= True
        self.running= False
        self.animation_time=0
        self.frame_index=0
        self.current_animation= "idle_right" 
        self.get_sprite_list()

    def draw(self, screen):
        #pygame.draw.rect(screen,"blue", self.rect)
        screen.blit(self.image,(self.rect))

    def move_x(self, key, previous_x):
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
            self.direction= "left"

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
            self.direction= "right"

        # Check whether player is moving
        if (previous_x!=self.rect.x):
                #Set animation to run animation
                self.running= True
                self.idle=False
        else:
            #Set animation to idle animation
            self.idle=True
            self.running= False


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

    def animate(self, delta_time):
        animation = self.animations[self.current_animation]

        self.animation_time += delta_time
        frame_duration = 0.2

        if self.animation_time >= frame_duration:
            self.animation_time = 0
            self.frame_index += 1

            if self.frame_index >= len(animation):
                self.frame_index = 0

        self.image = animation[self.frame_index]

    def get_sprite_list(self):
        self.animations = {}

        sprite_sheet_image_1 = pygame.image.load(
            "assets/tiles/sprites/hero_16x16_idle_spriteSheet.png"
        ).convert_alpha()

        sprite_sheet_image_2 = pygame.image.load(
            "assets/tiles/sprites/hero_16x16_rpgm23k_spritesheet.png"
        ).convert_alpha()

        idle_animation_steps = 2
        run_animation_steps = 3
        # Idle animation
        # 8x1 sheet: 4 directions × 2 frames
        directions = ["front", "right", "left", "back"]

        for dir_index, direction in enumerate(directions):
            idle_animation = []

            for x in range(idle_animation_steps):
                animation_image = pygame.Surface((p_size, p_size), pygame.SRCALPHA)

                sheet_x = (dir_index * idle_animation_steps + x) * p_size
                sheet_y = 0

                animation_image.blit(
                    sprite_sheet_image_1,
                    (0, 0),
                    (sheet_x, sheet_y, p_size, p_size)
                )

                idle_animation.append(animation_image)

            self.animations[f"idle_{direction}"] = idle_animation
        # Run animation
        # 3x4 sheet: 3 frames per row)
        directions = ["back", "right", "front", "left"]

        for row, direction in enumerate(directions):
            run_animation = []

            for x in range(run_animation_steps):
                animation_image = pygame.Surface((p_size, p_size), pygame.SRCALPHA)

                sheet_x = x * p_size
                sheet_y = row * p_size

                animation_image.blit(
                    sprite_sheet_image_2,
                    (0, 0),
                    (sheet_x, sheet_y, p_size, p_size)
                )

                run_animation.append(animation_image)

            self.animations[f"run_{direction}"] = run_animation


    def get_current_animation(self):
        new_animation = self.current_animation 
        if(self.idle==True) and (self.direction=="left"):
                    new_animation ="idle_left"
        elif (self.idle==True) and (self.direction=="right"):
                    new_animation ="idle_right"
        elif (self.idle==False) and (self.direction=="left"):
                    new_animation ="run_left"
        elif (self.idle==False) and (self.direction=="right"):
                    new_animation ="run_right"
        if new_animation != self.current_animation:
            self.current_animation = new_animation
            self.frame_index = 0
        

    def update(self,key,delta_time):
        self.move_x(key, self.rect.x)
        self.move_y(key)
        self.get_current_animation()
        self.animate(delta_time)

