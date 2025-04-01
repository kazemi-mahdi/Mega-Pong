import json
from menu import MenuSystem
import pygame
from GameMenu import Game
from Pong import Pong
from TetraPong import TetraPong
from HexaPong import HexaPong
from settings import Settings
# import tkinter as tk

# MegaPong = Pong()
# MegaPong = TetraPong()
# MegaPong = HexaPong()
# MegaPong.run_game()
# g = Game()
# # while g.running:
# #     g.curr_menu.display_menu()
# #     g.game_loop()
# g.curr_menu.display_menu()
# g.game_loop()
if __name__ == "__main__":
    # create a window using tkinter (the game menu)
    # window = tk.Tk()
    pygame.init()
    settings = Settings()

    pygame.init()

    #create game window
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 324

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Main Menu")

    # menu = menu_system(SCREEN_WIDTH, SCREEN_HEIGHT, screen)

    menus = MenuSystem(SCREEN_WIDTH, SCREEN_HEIGHT, screen)
    #game loop
    run = True
    while run:
        screen.fill((52, 78, 91))
        
        menus.Draw_MainMenu()
        # menus.scroll += 4
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        pygame.display.update()
        
    pygame.quit()

    # def play_theme():
    #     pygame.mixer.Sound.play(settings.main_menu_theme)


    # def stop_theme():
    #     pygame.mixer.quit()


    # def start_pong():
    #     stop_theme()
    #     window.destroy()
    #     MegaPong = Pong()
    #     MegaPong.run_game()


    # def start_tetra_pong():
    #     stop_theme()
    #     window.destroy()
    #     MegaPong = TetraPong()
    #     MegaPong.run_game()


    # def start_hexa_pong():
    #     stop_theme()
    #     window.destroy()
    #     MegaPong = HexaPong()
    #     MegaPong.run_game()


    # def get_high_score(game_name):
    #     try:
    #         with open("Assets/high_score/high_score.json", "r") as file:
    #             json_data = json.load(file)
    #             high_score = json_data[game_name]
    #             return high_score
    #     except FileNotFoundError:
    #         pass

    # def show_high_score():
    #     for widget in window.winfo_children():
    #         widget.destroy()

    #     tk.Label(window, text=f"Pong Score : {get_high_score('pong_high_score')}", font=("Arial", 30), fg="#c8c8c8", bg="#1F1F1F").place(x=100, y=150)
    #     tk.Label(window, text=f"Pong Score : {get_high_score('tetra_pong_high_score')}", font=("Arial", 30), fg="#c8c8c8", bg="#1F1F1F").place(x=100, y=200)
    #     tk.Label(window, text=f"Pong Score : {get_high_score('hexa_pong_high_score')}", font=("Arial", 30), fg="#c8c8c8", bg="#1F1F1F").place(x=100, y=250)


    # window.title("MegaPong")
    # window_width, window_height = 500, 500
    # window.geometry(f"{window_width}x{window_height}")
    # # disable resizing of the window
    # window.resizable(False, False)
    # # bg color (grey 12 pygame) = #1F1F1F
    # # text color (200, 200, 200) = #c8c8c8
    # window["bg"] = "#1F1F1F"


    # def game_menu():
    #     for widget in window.winfo_children():
    #         widget.destroy()
    #     # create a label
    #     label = tk.Label(window, text="Select a Pong!", font=("Arial", 30), fg="#c8c8c8", bg="#1F1F1F")
    #     label.place(x=150, y=50)

    #     # create buttons
    #     pong_button = tk.Button(window, text="Pong", font=("Arial", 20), fg="#c8c8c8", bg="#1F1F1F", command=start_pong)
    #     pong_button.place(x=200, y=150)

    #     tetra_pong_button = tk.Button(window, text="Tetra Pong", font=("Arial", 20), fg="#c8c8c8", bg="#1F1F1F",
    #                                   command=start_tetra_pong)
    #     tetra_pong_button.place(x=200, y=250)

    #     hexa_pong_button = tk.Button(window, text="Hexa Pong", font=("Arial", 20), fg="#c8c8c8", bg="#1F1F1F",
    #                                  command=start_hexa_pong)
    #     hexa_pong_button.place(x=200, y=350)


    # def main_menu():

    #     # create a label
    #     label = tk.Label(window, text="MegaPong", font=("Arial", 30), fg="#c8c8c8", bg="#1F1F1F")
    #     label.place(x=150, y=50)

    #     # create buttons
    #     play_button = tk.Button(window, text="Play", font=("Arial", 20), fg="#c8c8c8", bg="#1F1F1F", command=game_menu)
    #     play_button.place(x=200, y=150)

    #     hig_score_button = tk.Button(window, text="highest score", font=("Arial", 20), fg="#c8c8c8", bg="#1F1F1F",
    #                                  command=show_high_score)
    #     hig_score_button.place(x=200, y=250)

    #     quit_button = tk.Button(window, text="Quit", font=("Arial", 20), fg="#c8c8c8", bg="#1F1F1F",
    #                             command=window.quit)
    #     quit_button.place(x=200, y=350)


    # play_theme()
    # main_menu()

    # window.mainloop()
