import sys

import pygame
from menu import *
from settings import Settings
from Pong import Pong


class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

        self.settings = Settings()

        self.DISPLAY_W, self.DISPLAY_H = self.settings.screen_full_width, self.settings.screen_full_height
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H))
        # self.font_name = '8-BIT WONDER.TTF'
        self.font_name = pygame.font.get_default_font()
        self.BLACK, self.WHITE = (0, 0, 0), (200, 200, 200)

        self.clock = pygame.time.Clock()

        self.main_menu = MainMenu(self)
        self.game_menu = GameMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.curr_menu = self.main_menu

        self.pong = Pong()

    def game_loop(self):
        while self.playing:
            self.clock.tick(self.settings.FPS)
            self.check_events()
            self.game_menu.check_input()
            if self.START_KEY:
                self.playing = False
            self.display.fill(self.BLACK)
            self.draw_text("Select the game", 20, self.DISPLAY_W / 2, self.DISPLAY_H / 2 - 20)
            self.draw_text("Pong", 20, self.game_menu.pong_x, self.game_menu.pong_y)
            self.draw_text("Tetra Pong", 20, self.game_menu.tetra_pong_x, self.game_menu.tetra_pong_y)
            self.draw_text("Hexa Pong", 20, self.game_menu.hexa_pong_x, self.game_menu.hexa_pong_y)
            # self.window.blit(self.display, (0, 0))
            pygame.display.update()
            self.game_menu.draw_cursor()
            self.game_menu.blit_screen()
            self.reset_keys()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    self.running, self.playing = False, False
                    self.curr_menu.run_display = False
                    sys.exit()
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)