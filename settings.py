from math import sqrt, pi, ceil, cos, sin, tan, radians

import pygame


class Settings:
    """A class to store all settings for Mega Pong."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_full_width = pygame.display.Info().current_w
        self.screen_full_height = pygame.display.Info().current_h
        self.screen_half_width = self.screen_full_width / 2
        self.screen_half_height = self.screen_full_height / 2

        self.FPS = 60  # frames per second

        # Color
        self.white = pygame.Color("white")
        self.black = pygame.Color("black")
        self.bg_color = pygame.Color("grey12")
        self.light_grey = (200, 200, 200)

        # Wall settings
        self.goldenRatio = ((1 + sqrt(5)) / 2) - 1
        self.PI = pi

        self.useless_area = (ceil(
            self.screen_full_width - (self.screen_full_height / self.goldenRatio)) / 2)  # The useless area
        self.usefull_area = ceil((self.screen_full_height / self.goldenRatio))  # The usefull area

        self.wall_thickness = 5  # in pixels

        self.wall_length = ceil(self.screen_full_height / (sqrt(3) + 1))  # The length of the walls
        self.wall_half_length = self.wall_length / 2  # The half-length of the walls

        self.wall_side_cos = cos(self.PI / 6) * self.wall_length  # The length of the walls' side
        self.wall_side_sin = sin(self.PI / 6) * self.wall_length  # The length of the walls' side

        self.half_wall_side_cos = cos(self.PI / 6) * self.wall_length / 2  # The half-length of the walls' side
        self.half_wall_side_sin = sin(self.PI / 6) * self.wall_length / 2  # The half-length of the walls' side

        self.top_bottom_wall_length = self.screen_full_width - (self.useless_area * 2) - (self.wall_side_sin * 2)

        # Wall cordinates (center)
        self.top_left_x = self.useless_area + self.half_wall_side_sin
        self.top_left_y = self.half_wall_side_cos

        self.left_x = self.useless_area
        self.left_y = self.wall_half_length + self.wall_side_cos

        self.bottom_left_x = self.useless_area + self.half_wall_side_sin
        self.bottom_left_y = self.screen_full_height - self.half_wall_side_cos

        self.top_right_x = self.screen_full_width - self.useless_area - self.half_wall_side_sin
        self.top_right_y = self.half_wall_side_cos

        self.right_x = self.screen_full_width - self.useless_area
        self.right_y = self.wall_half_length + self.wall_side_cos

        self.bottom_right_x = self.screen_full_width - self.useless_area - self.half_wall_side_sin
        self.bottom_right_y = self.screen_full_height - self.half_wall_side_cos

        self.top_x = self.screen_full_width // 2
        self.top_y = 0

        self.bottom_x = self.screen_full_width // 2
        self.bottom_y = self.screen_full_height

        # Ball settings
        self.ball_speed = 10  # in pixels per frame

        # Paddle settings
        self.paddle_width = 10  # in pixels
        self.paddle_height = self.wall_half_length  # in pixels
        self.paddle_speed = 10  # in pixels per frame
        self.paddle_speed_x = 0.5 * 10  # in pixels per frame
        self.paddle_speed_y = 0.8 * 10  # in pixels per frame
        self.paddle_distance = 40 # in pixels
        self.paddle_distance_x = self.paddle_distance / sin(self.PI / 3) # in pixels
        self.paddle_distance_y = self.paddle_distance / cos(self.PI / 3) # in pixels
        self.paddle_x_distance = sqrt(self.paddle_distance ** 2 / (1 + tan(pi / 6) ** 2))
        self.paddle_y_distance = sqrt(self.paddle_distance ** 2 - self.paddle_x_distance ** 2)

        # Paddle cordinates (center)
        self.top_left_paddle_x = self.top_left_x + self.paddle_x_distance
        self.top_left_paddle_y = self.top_left_y + self.paddle_y_distance

        self.top_right_paddle_x = self.top_right_x - self.paddle_x_distance
        self.top_right_paddle_y = self.top_right_y + self.paddle_y_distance

        self.bottom_left_paddle_x = self.bottom_left_x + self.paddle_x_distance
        self.bottom_left_paddle_y = self.bottom_left_y - self.paddle_y_distance

        self.bottom_right_paddle_x = self.bottom_right_x - self.paddle_x_distance
        self.bottom_right_paddle_y = self.bottom_right_y - self.paddle_y_distance

        self.right_paddle_x = self.right_x - self.paddle_distance
        self.right_paddle_y = self.right_y

        self.left_paddle_x = self.left_x + self.paddle_distance
        self.left_paddle_y = self.left_y

        self.upper_right_paddle_x = self.right_x - self.paddle_distance
        self.upper_right_paddle_y = self.top_right_y

        self.lower_right_paddle_x = self.right_x - self.paddle_distance
        self.lower_right_paddle_y = self.bottom_right_y

        self.upper_left_paddle_x = self.left_x + self.paddle_distance
        self.upper_left_paddle_y = self.top_left_y

        self.lower_left_paddle_x = self.left_x + self.paddle_distance
        self.lower_left_paddle_y = self.bottom_left_y


        ####################
        #sound settings
        self.main_menu_theme = pygame.mixer.Sound("Assets/soundtracks/main menu.wav")
        self.selection_circle_sound = pygame.mixer.Sound("Assets/soundtracks/selection circles.wav")
        self.selected_sound = pygame.mixer.Sound("Assets/soundtracks/selected.wav")
        self.paddle_hit_sound = pygame.mixer.Sound("Assets/soundtracks/hit-new.wav")
        self.wall_hit_sound = pygame.mixer.Sound("Assets/soundtracks/ball fall.wav")

