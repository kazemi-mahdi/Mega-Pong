import os

import pygame
from pygame.sprite import Sprite


class Wall(Sprite):
    def __init__(self, settings, centerx, centery, angle, wall_length, wall_thickness, wall_name):
        super().__init__()
        self.settings = settings
        self.wall_length = wall_length
        self.wall_thickness = wall_thickness
        self.wall_name = wall_name
        self.image = pygame.image.load(os.path.join("./Assets/images", "light_grey.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.wall_length, self.wall_thickness))
        self.image = pygame.transform.rotate(self.image, angle)
        self.image_mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect.center = [centerx, centery]


def create_all_walls(settings):
    all_walls_sprites = pygame.sprite.Group()

    # Right and Left walls
    top_left = Wall(settings, settings.top_left_x, settings.top_left_y, 60,
                    settings.wall_length, settings.wall_thickness, "top_left")

    left = Wall(settings, settings.left_x, settings.left_y, 90,
                settings.wall_length, settings.wall_thickness, "left")

    bottom_left = Wall(settings, settings.bottom_left_x,
                       settings.bottom_left_y, 300, settings.wall_length,
                       settings.wall_thickness, "bottom_left")

    top_right = Wall(settings, settings.top_right_x,
                     settings.top_right_y, 300, settings.wall_length, settings.wall_thickness, "top_right")

    right = Wall(settings, settings.right_x,
                 settings.right_y, 90, settings.wall_length, settings.wall_thickness, "right")

    bottom_right = Wall(settings, settings.bottom_right_x,
                        settings.bottom_right_y, 60, settings.wall_length,
                        settings.wall_thickness, "bottom_right")

    # Top and Bottom walls
    top = Wall(settings, settings.top_x, settings.top_y, 0,
               settings.top_bottom_wall_length, settings.wall_thickness, "top")

    bottom = Wall(settings, settings.bottom_x, settings.bottom_y, 0,
                  settings.top_bottom_wall_length, settings.wall_thickness, "bottom")

    # Adding walls to the group
    all_walls_sprites.add(top_left)
    all_walls_sprites.add(left)
    all_walls_sprites.add(bottom_left)
    all_walls_sprites.add(bottom_right)
    all_walls_sprites.add(right)
    all_walls_sprites.add(top_right)
    all_walls_sprites.add(top)
    all_walls_sprites.add(bottom)

    return all_walls_sprites


def create_all_pong_walls(settings):
    all_walls_sprites = pygame.sprite.Group()

    # Right and Left walls
    left = Wall(settings, settings.left_x, settings.left_y, 90,
                settings.screen_full_height, settings.wall_thickness, "left")

    right = Wall(settings, settings.right_x,settings.right_y, 90,
                 settings.screen_full_height, settings.wall_thickness, "right")

    # Top and Bottom walls
    top = Wall(settings, settings.top_x, settings.top_y, 0,
               settings.usefull_area, settings.wall_thickness, "top")

    bottom = Wall(settings, settings.bottom_x, settings.bottom_y, 0,
                  settings.usefull_area, settings.wall_thickness, "bottom")

    # Adding walls to the group
    all_walls_sprites.add(left)
    all_walls_sprites.add(right)
    all_walls_sprites.add(top)
    all_walls_sprites.add(bottom)

    return all_walls_sprites
