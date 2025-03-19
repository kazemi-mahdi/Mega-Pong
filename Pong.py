import os
import json
import sys

import pygame

from Gamestats import Gamestats
from ball import Ball
from scoreboard import Scoreboard
from settings import Settings
from wall import create_all_pong_walls
from paddles import create_all_pong_paddles


class Pong:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""

        self.playing_pong = False

        # menu variables for game state
        self.running = True
        self.playing = False
        # menu variables (moving)
        self.UP_KEY = False
        self.DOWN_KEY = False
        self.START_KEY = False
        self.BACK_KEY = False

        # Initialize Pygame, settings, and screen object.
        pygame.init()

        # initialize the joystick
        pygame.joystick.init()

        # create a joystick
        self.joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

        #  because of interference i only initialize two joysticks(ps4 controller)
        # self.joysticks = [pygame.joystick.Joystick(i) for i in range(2)]
        for joystick in self.joysticks:
            print(f"name: {joystick.get_name()} id: {joystick.get_id()} instance: {joystick.get_instance_id()}")

        # loading ps4 controller map
        with open(os.path.join("Assets/controller map", "PS4 Controller.json"), 'r+') as file:
            self.ps4_keys = json.load(file)

        # loading twin usb joystick map
        with open(os.path.join("Assets/controller map", "Twin USB Joystick.json"), 'r+') as file:
            self.twin_usb = json.load(file)

        # creating settings object
        self.settings = Settings()

        # setting game caption
        pygame.display.set_caption("Pong")

        # setting game display
        self.display = pygame.Surface((self.settings.screen_full_width, self.settings.screen_full_height))
        self.screen = pygame.display.set_mode((self.settings.screen_full_width, self.settings.screen_full_height))

        # Create a list of walls
        self.all_walls_sprites = create_all_pong_walls(self.settings)

        # Create a list of paddles
        self.all_paddles_group = create_all_pong_paddles(self)

        # Create a list of balls
        self.all_balls_sprites = pygame.sprite.Group()
        ball = Ball(self.settings, self.settings.light_grey, 15, 15)
        self.all_balls_sprites.add(ball)

        # Create a scoreboard
        self.stats = Gamestats(self)
        self.score_board = Scoreboard(self)

        # Create a clock for FPS
        self.clock = pygame.time.Clock()

    def run_game(self):
        """Start the main loop for the game."""
        # while self.playing_pong:
        while True:
            # FPS Limit
            self.clock.tick(self.settings.FPS)
            self._check_events()
            if self.START_KEY:
                self.playing = False
            for paddle in self.all_paddles_group:
                paddle.pong_update()
            self._update_balls()
            self._update_screen()
            self._reset_keys()

    def _reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
                sys.exit()
            elif event.type == pygame.JOYBUTTONDOWN:
                self._check_joystick_keydown_events(event)
            elif event.type == pygame.JOYBUTTONUP:
                self._check_joystick_keyup_events(event)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.JOYBUTTONDOWN:
                print(event)

    def _check_joystick_keydown_events(self, event):
        """Respond to keypresses."""
        self.id = event.instance_id
        for joystick in self.joysticks:
            if event.button == self.ps4_keys["up_arrow"] or event.button == self.twin_usb["one"]:
                self.all_paddles_group[self.id % 2].moving_up = True
            elif event.button == self.ps4_keys["down_arrow"] or event.button == self.twin_usb["three"]:
                self.all_paddles_group[self.id % 2].moving_down = True
            # if joystick.get_name == "PS4 Controller":
            #     print("ok")
            #     if event.button == self.ps4_keys["triangle"] or event.button == self.ps4_keys["up_arrow"]:
            #         self.all_paddles_group[self.id % 2].moving_up = True
            #     elif event.button == self.ps4_keys["x"] or event.button == self.ps4_keys["down_arrow"]:
            #         self.all_paddles_group[self.id % 2].moving_down = True
            # else:
            #     if event.button == self.twin_usb["one"]:
            #         self.all_paddles_group[self.id % 2].moving_up = True
            #     elif event.button == self.twin_usb["three"]:
            #         self.all_paddles_group[self.id % 2].moving_down = True

    def _check_joystick_keyup_events(self, event):
        """Respond to key releases."""
        self.id = event.instance_id
        if event.button == self.ps4_keys["up_arrow"] or event.button == self.twin_usb["one"]:
            self.all_paddles_group[self.id % 2].moving_up = False
        elif event.button == self.ps4_keys["down_arrow"] or event.button == self.twin_usb["three"]:
            self.all_paddles_group[self.id % 2].moving_down = False
        # for joystick in self.joysticks:
        #     if joystick.get_name == "PS4 Controller":
        #         if event.button == self.ps4_keys["triangle"] or event.button == self.ps4_keys["up_arrow"]:
        #             self.all_paddles_group[self.id % 2].moving_up = False
        #         elif event.button == self.ps4_keys["x"] or event.button == self.ps4_keys["down_arrow"]:
        #             self.all_paddles_group[self.id % 2].moving_down = False
        #     else:
        #         if event.button == self.twin_usb["one"]:
        #             self.all_paddles_group[self.id % 2].moving_up = False
        #         elif event.button == self.twin_usb["three"]:
        #             self.all_paddles_group[self.id % 2].moving_down = False

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_ESCAPE or event.key == pygame.K_x:
            sys.exit()
        elif event.key == pygame.K_RETURN:
            self.START_KEY = True
        elif event.key == pygame.K_BACKSPACE:
            self.BACK_KEY = True
        elif event.key == pygame.K_DOWN:
            self.DOWN_KEY = True
        elif event.key == pygame.K_UP:
            self.UP_KEY = True
        # right paddle , index = 0
        elif event.key == pygame.K_q:
            self.all_paddles_group[0].moving_up = True
        elif event.key == pygame.K_a:
            self.all_paddles_group[0].moving_down = True
        # left paddle, index = 1
        elif event.key == pygame.K_w:
            self.all_paddles_group[1].moving_up = True
        elif event.key == pygame.K_s:
            self.all_paddles_group[1].moving_down = True

    def _check_keyup_events(self, event):
        """Respond to key releases."""

        # right paddle , index 0
        if event.key == pygame.K_q:
            self.all_paddles_group[0].moving_up = False
        elif event.key == pygame.K_a:
            self.all_paddles_group[0].moving_down = False
        # left paddle, index 1
        elif event.key == pygame.K_w:
            self.all_paddles_group[1].moving_up = False
        elif event.key == pygame.K_s:
            self.all_paddles_group[1].moving_down = False

    def _check_ball_collisions(self):
        """Check for collisions"""

        # ball Collision with right and left walls
        for wall in self.all_walls_sprites:
            for ball in self.all_balls_sprites:
                if wall.wall_name != "top" and wall.wall_name != "bottom" and pygame.sprite.collide_mask(wall, ball):
                    pygame.mixer.Sound.play(self.settings.wall_hit_sound)
                    if wall.wall_name == "right" or wall.wall_name == "top_right" or wall.wall_name == "bottom_right":
                        self.stats.left_score += 1
                        self.score_board.prep_score()
                        print("Yea")
                    elif wall.wall_name == "left" or wall.wall_name == "top_left" or wall.wall_name == "bottom_left":
                        self.stats.right_score += 1
                        self.score_board.prep_score()
                        print("poa")

                    ball.reset_position()
                elif pygame.sprite.collide_mask(wall, ball):
                    ball.y_bounce()

        # ball Collision with paddles
        for paddle in self.all_paddles_group:
            for ball in self.all_balls_sprites:
                if pygame.sprite.collide_mask(paddle, ball):
                    pygame.mixer.Sound.play(self.settings.paddle_hit_sound)
                    ball.change_movement_angel()
                    ball.x_bounce()
                    ball.y_bounce()

        # for paddle in self.all_paddles_group:
        #     for ball in self.all_balls_sprites:
        #         offset = (ball.rect.centerx - paddle.rect.centerx, ball.rect.centery - paddle.rect.centery)
        #         if paddle.mask.overlap(ball.mask, offset):
        #             ball.x_bounce()

    def _update_balls(self):
        self._check_ball_collisions()
        self.all_balls_sprites.update()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.all_walls_sprites.draw(self.screen)
        self.all_balls_sprites.draw(self.screen)
        for paddle in self.all_paddles_group:
            paddle.blitme()

        # Draw the score
        self.score_board.show_score()
        pygame.display.flip()