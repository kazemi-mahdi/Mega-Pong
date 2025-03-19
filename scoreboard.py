import os
# from Gamestats import Gamestats

import pygame.font


class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, mp_game):
        """Initialize scorekeeping attributes."""
        # creating an object of Gamestats class for saving high score
        # self.stats = Gamestats(mp_game)

        self.screen = mp_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = mp_game.settings
        self.stats = mp_game.stats

        # attributes needed in next parts
        self.right_score = None
        self.left_score = None
        self.left_score_rect = None
        self.left_score_image = None
        self.right_score_image = None
        self.right_score_rect = None

        # Font settings for scoring information.
        self.text_color = (255, 255, 255)
        self.font = pygame.font.Font(os.path.join("Assets/fonts/", "Arcade_font.ttf"), 40)

        # Prepare the initial score image.
        self.prep_score()

    def prep_score(self):
        """Turn the score into a rendered image."""
        right_score_str = f"{str(self.stats.right_score)}"
        self.right_score_image = self.font.render(right_score_str, True, self.text_color)
        # Display the score at the top right of the screen.
        self.right_score_rect = self.right_score_image.get_rect()
        self.right_score_rect.centerx = self.settings.screen_full_width // 2 + 100
        self.right_score_rect.top = 30

        left_score_str = f"{str(self.stats.left_score)}"
        self.left_score_image = self.font.render(left_score_str, True, self.text_color)
        # Display the score at the top right of the screen.
        self.left_score_rect = self.left_score_image.get_rect()
        self.left_score_rect.centerx = self.settings.screen_full_width // 2 - 100
        self.left_score_rect.top = 30

    def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.right_score_image, self.right_score_rect)
        self.screen.blit(self.left_score_image, self.left_score_rect)

        # Draw middle line
        pygame.draw.line(self.screen, self.text_color, (self.settings.screen_full_width // 2, 0),
                         (self.settings.screen_full_width // 2, self.settings.screen_full_height), 5)
