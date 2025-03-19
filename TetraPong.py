import os
import json
import sys

import pygame

from Gamestats import Gamestats
from ball import Ball
from scoreboard import Scoreboard
from settings import Settings
from wall import create_all_pong_walls
from paddles import create_all_tetra_pong_paddles


class TetraPong:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        # initialize the joystick
        pygame.joystick.init()
        # create a joystick
        # self.joystick = pygame.joystick.Joystick(0)
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
        self.settings = Settings()

        pygame.display.set_caption("Tetra Pong")

        self.screen = pygame.display.set_mode((self.settings.screen_full_width, self.settings.screen_full_height))

        # Create a list of walls
        self.all_walls_sprites = create_all_pong_walls(self.settings)

        # Create a list of paddles
        self.all_paddles_group = create_all_tetra_pong_paddles(self)

        # Create a list of balls
        self.all_balls_sprites = pygame.sprite.Group()
        ball = Ball(self.settings, self.settings.light_grey, 15, 15)
        self.all_balls_sprites.add(ball)

        self.stats = Gamestats(self)
        self.score_board = Scoreboard(self)

        self.clock = pygame.time.Clock()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # FPS Limit
            self.clock.tick(self.settings.FPS)
            for paddle in self.all_paddles_group:
                paddle.tetra_pong_update()
            self._check_events()
            self._update_balls()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
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
                self.all_paddles_group[self.id].moving_up = True
            elif event.button == self.ps4_keys["down_arrow"] or event.button == self.twin_usb["three"]:
                self.all_paddles_group[self.id].moving_down = True

    def _check_joystick_keyup_events(self, event):
        """Respond to keypresses."""
        self.id = event.instance_id
        if event.button == self.ps4_keys["up_arrow"] or event.button == self.twin_usb["one"]:
            self.all_paddles_group[self.id].moving_up = False
        elif event.button == self.ps4_keys["down_arrow"] or event.button == self.twin_usb["three"]:
            self.all_paddles_group[self.id].moving_down = False

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_ESCAPE or event.key == pygame.K_x:
            sys.exit()

        # top right paddle , index = 0
        elif event.key == pygame.K_q:
            self.all_paddles_group[0].moving_up = True
        elif event.key == pygame.K_a:
            self.all_paddles_group[0].moving_down = True
        # bottom right paddle, index = 1
        elif event.key == pygame.K_w:
            self.all_paddles_group[1].moving_up = True
        elif event.key == pygame.K_s:
            self.all_paddles_group[1].moving_down = True
        # top left paddle, index = 2
        elif event.key == pygame.K_t:
            self.all_paddles_group[2].moving_up = True
        elif event.key == pygame.K_g:
            self.all_paddles_group[2].moving_down = True
        # bottom left paddle, index = 3
        elif event.key == pygame.K_y:
            self.all_paddles_group[3].moving_up = True
        elif event.key == pygame.K_h:
            self.all_paddles_group[3].moving_down = True

        # joystick events
        # elif event.type == pygame.JOYBUTTONDOWN:
        #     print(event)

    def _check_keyup_events(self, event):
        """Respond to key releases."""

        # top right paddle , index = 0
        if event.key == pygame.K_q:
            self.all_paddles_group[0].moving_up = False
        elif event.key == pygame.K_a:
            self.all_paddles_group[0].moving_down = False
        # bottom right paddle, index = 1
        elif event.key == pygame.K_w:
            self.all_paddles_group[1].moving_up = False
        elif event.key == pygame.K_s:
            self.all_paddles_group[1].moving_down = False
        # top left paddle, index = 2
        elif event.key == pygame.K_t:
            self.all_paddles_group[2].moving_up = False
        elif event.key == pygame.K_g:
            self.all_paddles_group[2].moving_down = False
        # bottom left paddle, index = 3
        elif event.key == pygame.K_y:
            self.all_paddles_group[3].moving_up = False
        elif event.key == pygame.K_h:
            self.all_paddles_group[3].moving_down = False

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
