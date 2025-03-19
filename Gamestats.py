import os
from settings import Settings
import json


class Gamestats:
    def __init__(self, mp_game):
        """Initialize statistics."""
        self.settings = mp_game.settings
        self.reset_stats()

        # Start game in an inactive state.
        self.game_active = False

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.right_score = 0
        self.left_score = 0
        self.total_level = 1
        # self.get_high_score()

    # def get_high_score(self, game_name):
    #     try:
    #         with open("Assets/high_score/high_score.json", "r") as file:
    #             json_data = json.load(file)
    #             self.high_score = json_data[f"{game_name}_high_score"]
    #
    #     except FileNotFoundError:
    #         self.high_score = 0

    # def save_high_score(self, game_name):
    #     try:
    #         with open("Assets/high_score/high_score.json", "r") as file:
    #             json_data = json.load(file)
    #             self.high_score = json_data[f"{game_name}_high_score"]
    #
    #     except FileNotFoundError:
    #         self.high_score = 0
    #
    #     if self.score > self.high_score:
    #         # Data to be written
    #         dictionary = {
    #             f"{game_name}_high_score": self.score
    #         }
    #
    #         with open("Assets/high_score/high_score.json", "w") as file:
    #             json.dump(dictionary, file, indent=4)