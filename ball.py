import os
from math import pi, cos, sin

import pygame
from pygame.sprite import Sprite
import random


class Ball(Sprite):
    def __init__(self, settings, color, width, height):
        super().__init__()

        self.settings = settings
        self.color = color
        self.width = width
        self.height = height

        # Create a ball rect at (0, 0) and then set correct position.
        self.image = pygame.image.load(os.path.join("./Assets/images", "ball.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

        # move to right or left
        self.move_to = random.choice(["top_right", "top_left", "bottom_right", "bottom_left"])
        if self.move_to == "top_right":
            self.change_x = 1
            self.change_y = 1
        elif self.move_to == "top_left":
            self.change_x = -1
            self.change_y = 1
        elif self.move_to == "bottom_right":
            self.change_x = 1
            self.change_y = -1
        elif self.move_to == "bottom_left":
            self.change_x = -1
            self.change_y = -1

        # movement angel
        self.movement_angel_in_degrees = random.randint(30, 70)
        self.movement_angel_in_radians = (self.movement_angel_in_degrees * pi / 180)

        # Locating the ball
        self.rect.center = (self.settings.screen_full_width // 2, self.settings.screen_full_height // 2)

        # Store the ball's exact horizontal and vertical position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])
        # if self.movement_angel_in_degrees == 90 or self.movement_angel_in_degrees == 0:
        #     self.reset_position()
        self.x += self.settings.ball_speed * cos(self.movement_angel_in_radians) * self.change_x
        self.y += self.settings.ball_speed * sin(self.movement_angel_in_radians) * self.change_y

        self.rect.x, self.rect.y = self.x, self.y

    def change_movement_angel(self):
        self.movement_angel_in_degrees = random.randint(30, 70)
        self.movement_angel_in_radians = (self.movement_angel_in_degrees * pi / 180)

    def y_bounce(self):
        self.change_y *= -1

    def x_bounce(self):
        self.change_x *= -1

    def reset_position(self):
        self.move_to = random.choice(["right", "left"])
        self.movement_angel_in_degrees = random.randint(20, 160)
        self.movement_angel_in_radians = (self.movement_angel_in_degrees * pi / 180)
        self.rect.center = (self.settings.screen_full_width // 2, self.settings.screen_full_height // 2)
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
