import os
import math

import pygame
from pygame.sprite import Sprite


class Paddle:
    def __init__(self, name, paddle_angle, mp_game):
        self.name = name
        self.paddle_angle = paddle_angle
        self.screen = mp_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = mp_game.settings

        # Load the Paddle
        self.image = pygame.image.load(os.path.join("./Assets/images", "light_grey.png")).convert_alpha()
        # scaling the paddle
        self.image = pygame.transform.scale(self.image,
                                            (self.settings.paddle_width, self.settings.paddle_height))
        # rotating the paddle
        self.image = pygame.transform.rotate(self.image, self.paddle_angle)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

        self.set_starting_position()

        # moving flags
        self.moving_up = False
        self.moving_down = False

    def set_starting_position(self):
        """Set the starting position of the paddle And rotate it"""
        if self.name == "top_right_paddle":
            self.rect.centerx = self.settings.top_right_paddle_x
            self.rect.centery = self.settings.top_right_paddle_y

        if self.name == "right_paddle":
            self.rect.centerx = self.settings.right_paddle_x
            self.rect.centery = self.settings.right_paddle_y

        if self.name == "bottom_right_paddle":
            self.rect.centerx = self.settings.bottom_right_paddle_x
            self.rect.centery = self.settings.bottom_right_paddle_y

        if self.name == "top_left_paddle":
            self.rect.centerx = self.settings.top_left_paddle_x
            self.rect.centery = self.settings.top_left_paddle_y

        if self.name == "left_paddle":
            self.rect.centerx = self.settings.left_paddle_x
            self.rect.centery = self.settings.left_paddle_y

        if self.name == "bottom_left_paddle":
            self.rect.centerx = self.settings.bottom_left_paddle_x
            self.rect.centery = self.settings.bottom_left_paddle_y

        if self.name == "upper_right_paddle":
            self.rect.centerx = self.settings.upper_right_paddle_x
            self.rect.centery = self.settings.upper_right_paddle_y

        if self.name == "lower_right_paddle":
            self.rect.centerx = self.settings.lower_right_paddle_x
            self.rect.centery = self.settings.lower_right_paddle_y

        if self.name == "upper_left_paddle":
            self.rect.centerx = self.settings.upper_left_paddle_x
            self.rect.centery = self.settings.upper_left_paddle_y

        if self.name == "lower_left_paddle":
            self.rect.centerx = self.settings.lower_left_paddle_x
            self.rect.centery = self.settings.lower_left_paddle_y

    def pong_update(self):
        if self.name == "right_paddle" and self.moving_up and self.rect.top > 0:
            self.rect.centery -= self.settings.paddle_speed
        if self.name == "right_paddle" and self.moving_down and self.rect.bottom < self.settings.screen_full_height:
            self.rect.centery += self.settings.paddle_speed

        if self.name == "left_paddle" and self.moving_up and self.rect.top > 0:
            self.rect.centery -= self.settings.paddle_speed
        if self.name == "left_paddle" and self.moving_down and self.rect.bottom < self.settings.screen_full_height:
            self.rect.centery += self.settings.paddle_speed

    def tetra_pong_update(self):
        if self.name == "upper_right_paddle" and self.moving_up and self.rect.top > 0:
            self.rect.centery -= self.settings.paddle_speed
        if self.name == "upper_right_paddle" and self.moving_down and self.rect.bottom < self.settings.screen_half_height:
            self.rect.centery += self.settings.paddle_speed

        if self.name == "lower_right_paddle" and self.moving_up and self.rect.top > self.settings.screen_half_height:
            self.rect.centery -= self.settings.paddle_speed
        if self.name == "lower_right_paddle" and self.moving_down and self.rect.bottom < self.settings.screen_full_height:
            self.rect.centery += self.settings.paddle_speed

        if self.name == "upper_left_paddle" and self.moving_up and self.rect.top > 0:
            self.rect.centery -= self.settings.paddle_speed
        if self.name == "upper_left_paddle" and self.moving_down and self.rect.bottom < self.settings.screen_half_height:
            self.rect.centery += self.settings.paddle_speed

        if self.name == "lower_left_paddle" and self.moving_up and self.rect.top > self.settings.screen_half_height:
            self.rect.centery -= self.settings.paddle_speed
        if self.name == "lower_left_paddle" and self.moving_down and self.rect.bottom < self.settings.screen_full_height:
            self.rect.centery += self.settings.paddle_speed

    # def offset(self, name, centery, centerx, angle):
    #     if name == "top_left_paddle":
    #         for x in range(math.ceil(self.settings.left_paddle_x), math.ceil(self.settings.useless_area + self.settings.wall_side_sin + self.settings.paddle_distance_x)):
    #             y = math.tan(math.radians(angle)) * (x - self.settings.left_paddle_x) * -1 + self.settings.left_paddle_y
    #             print(x, y)
    #             if abs(y - centery) > 0:
    #                 self.cordinates = [centerx, y]
    #                 return self.cordinates
    #             elif abs(y - centery) == 0:
    #                 self.cordinates = [centerx, centery]
    #                 return self.cordinates

    def update(self):
        if self.name == "top_right_paddle" and self.moving_up and self.rect.top > 0:
            self.rect.centery -= self.settings.paddle_speed_y
            self.rect.centerx -= self.settings.paddle_speed_x
        if self.name == "top_right_paddle" and self.moving_down and self.rect.bottom < self.settings.wall_side_cos:
            self.rect.centery += self.settings.paddle_speed_y
            self.rect.centerx += self.settings.paddle_speed_x

        if self.name == "right_paddle" and self.moving_up and self.rect.top > self.settings.wall_side_cos:
            self.rect.centery -= self.settings.paddle_speed
            if self.rect.top < self.settings.wall_side_cos:
                self.rect.top = self.settings.wall_side_cos
        if self.name == "right_paddle" and self.moving_down and self.rect.bottom < self.settings.wall_side_cos + self.settings.wall_length:
            self.rect.centery += self.settings.paddle_speed
            if self.rect.bottom > self.settings.wall_side_cos + self.settings.wall_length:
                self.rect.bottom = self.settings.wall_side_cos + self.settings.wall_length

        if self.name == "bottom_right_paddle" and self.moving_up and self.rect.top > self.settings.wall_side_cos + self.settings.wall_length:
            self.rect.centery -= self.settings.paddle_speed_y
            self.rect.centerx += self.settings.paddle_speed_x
        if self.name == "bottom_right_paddle" and self.moving_down and self.rect.bottom < self.settings.screen_full_height:
            self.rect.centery += self.settings.paddle_speed_y
            self.rect.centerx -= self.settings.paddle_speed_x

        if self.name == "top_left_paddle" and self.moving_up and self.rect.top > 0:
            self.rect.centery -= self.settings.paddle_speed_y
            self.rect.centerx += self.settings.paddle_speed_x
            # self.rect.centery -= self.settings.paddle_speed * math.sin(math.radians(30))
            # self.rect.centerx += self.settings.paddle_speed * math.cos(math.radians(30))
            # self.cord = self.offset("top_left_paddle", self.rect.centery, self.rect.centerx, 30)
            # self.rect.centery = self.cord[1]
            # self.rect.centerx = self.cord[0]
        if self.name == "top_left_paddle" and self.moving_down and self.rect.bottom < self.settings.wall_side_cos:
            self.rect.centery += self.settings.paddle_speed_y
            self.rect.centerx -= self.settings.paddle_speed_x
            # self.rect.centery += self.settings.paddle_speed * math.sin(math.radians(30))
            # self.rect.centerx -= self.settings.paddle_speed * math.cos(math.radians(30))
            # self.cord = self.offset("top_left_paddle", self.rect.centery, self.rect.centerx, -30)
            # self.rect.centery = self.cord[1]
            # self.rect.centerx = self.cord[0]

        if self.name == "left_paddle" and self.moving_up and self.rect.top > self.settings.wall_side_cos:
            self.rect.centery -= self.settings.paddle_speed
            if self.rect.top < self.settings.wall_side_cos:
                self.rect.top = self.settings.wall_side_cos
        if self.name == "left_paddle" and self.moving_down and self.rect.bottom < self.settings.wall_side_cos + self.settings.wall_length:
            self.rect.centery += self.settings.paddle_speed
            if self.rect.bottom > self.settings.wall_side_cos + self.settings.wall_length:
                self.rect.bottom = self.settings.wall_side_cos + self.settings.wall_length

        if self.name == "bottom_left_paddle" and self.moving_up and self.rect.top > self.settings.wall_side_cos + self.settings.wall_length:
            self.rect.centery -= self.settings.paddle_speed_y
            self.rect.centerx -= self.settings.paddle_speed_x
        if self.name == "bottom_left_paddle" and self.moving_down and self.rect.bottom < self.settings.screen_full_height:
            self.rect.centery += self.settings.paddle_speed_y
            self.rect.centerx += self.settings.paddle_speed_x

    def reset_position(self):
        if self.name == "top_right_paddle":
            pass
        if self.name == "right_paddle":
            pass
        if self.name == "bottom_right_paddle":
            pass
        if self.name == "top_left_paddle":
            pass
        if self.name == "left_paddle":
            pass
        if self.name == "bottom_left_paddle":
            pass

    def blitme(self):
        self.screen.blit(self.image, self.rect)


def create_all_paddles(mp_game):
    paddle_group = [
        Paddle("top_right_paddle", 30, mp_game),  # index number = 0
        Paddle("right_paddle", 0, mp_game),  # index number = 1
        Paddle("bottom_right_paddle", -30, mp_game),  # index number = 2
        Paddle("top_left_paddle", -30, mp_game),  # index number = 3
        Paddle("left_paddle", 0, mp_game),  # index number = 4
        Paddle("bottom_left_paddle", 30, mp_game)  # index number = 5
    ]

    return paddle_group


def create_all_pong_paddles(mp_game):
    paddle_group = [
        Paddle("right_paddle", 0, mp_game),  # index number = 0
        Paddle("left_paddle", 0, mp_game),  # index number = 1
    ]

    return paddle_group


def create_all_tetra_pong_paddles(mp_game):
    paddle_group = [
        Paddle("upper_right_paddle", 0, mp_game),  # index number = 0
        Paddle("lower_right_paddle", 0, mp_game),  # index number = 1
        Paddle("upper_left_paddle", 0, mp_game),  # index number = 2
        Paddle("lower_left_paddle", 0, mp_game)  # index number = 3
    ]

    return paddle_group


def create_all_hexa_pong_paddles(mp_game):
    paddle_group = [
        Paddle("top_right_paddle", 30, mp_game),  # index number = 0
        Paddle("right_paddle", 0, mp_game),  # index number = 1
        Paddle("bottom_right_paddle", -30, mp_game),  # index number = 2
        Paddle("bottom_left_paddle", 30, mp_game),  # index number = 3
        Paddle("left_paddle", 0, mp_game),  # index number = 4
        Paddle("top_left_paddle", -30, mp_game)  # index number = 5
    ]

    return paddle_group
