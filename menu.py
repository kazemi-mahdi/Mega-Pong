import pygame
import math
import os

class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 60

    def draw_cursor(self):
        self.game.draw_text('o', 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()


class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Play"
        self.play_x, self.play_y = self.mid_w, self.mid_h + 30
        self.credits_x, self.credits_y = self.mid_w, self.mid_h + 50
        self.quit_x, self.quit_y = self.mid_w, self.mid_h + 70
        self.cursor_rect.midtop = (self.play_x + self.offset, self.play_y)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            pygame.mixer.Sound.play(self.game.settings.main_menu_theme)
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Mega Pong', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text("Play", 20, self.play_x, self.play_y)
            self.game.draw_text("Credits", 20, self.credits_x, self.credits_y)
            self.game.draw_text("Quit", 20, self.quit_x, self.quit_y)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Play':
                self.cursor_rect.midtop = (self.credits_x + self.offset, self.credits_y)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.quit_x + self.offset, self.quit_y)
                self.state = 'Quit'
            elif self.state == 'Quit':
                self.cursor_rect.midtop = (self.play_x + self.offset, self.play_y)
                self.state = 'Play'
        elif self.game.UP_KEY:
            if self.state == 'Play':
                self.cursor_rect.midtop = (self.quit_x + self.offset, self.quit_y)
                self.state = 'Quit'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.play_x + self.offset, self.play_y)
                self.state = 'Play'
            elif self.state == 'Quit':
                self.cursor_rect.midtop = (self.credits_x + self.offset, self.credits_y)
                self.state = 'Credits'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Play':
                self.game.playing = True
                self.game.curr_menu = self.game.game_menu
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.options
            elif self.state == 'Quit':
                self.game.curr_menu = self.game.credits
            self.run_display = False

class GameMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

        # self.playing_pong = False
        # self.playing_tetra_pong = False
        # self.playing_hexa_pong = False

        self.state = "Play"
        self.pong_x, self.pong_y = self.mid_w, self.mid_h + 30
        self.tetra_pong_x, self.tetra_pong_y = self.mid_w, self.mid_h + 50
        self.hexa_pong_x, self.hexa_pong_y = self.mid_w, self.mid_h + 70
        self.cursor_rect.midtop = (self.pong_x + self.offset, self.pong_y)

    def display_menu(self):
        self.run_game_menu_display = False
        if self.run_game_menu_display:
            self.game.game_loop()
            # self.game.check_events()
            # self.check_input()
            # self.game.display.fill(self.game.BLACK)
            # self.game.draw_text("Select the game", 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            # self.game.draw_text("Pong", 20, self.pong_x, self.pong_y)
            # self.game.draw_text("Tetra Pong", 20, self.tetra_pong_x, self.tetra_pong_y)
            # self.game.draw_text("Hexa Pong", 20, self.hexa_pong_x, self.hexa_pong_y)
            # self.draw_cursor()
            # self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Pong':
                self.cursor_rect.midtop = (self.tetra_pong_x + self.offset, self.tetra_pong_y)
                self.state = 'Tetra Pong'
            elif self.state == 'Tetra Pong':
                self.cursor_rect.midtop = (self.hexa_pong_x + self.offset, self.hexa_pong_y)
                self.state = 'Hexa Pong'
            elif self.state == 'Hexa Pong':
                self.cursor_rect.midtop = (self.pong_x + self.offset, self.pong_y)
                self.state = 'Pong'
        elif self.game.UP_KEY:
            if self.state == 'Pong':
                self.cursor_rect.midtop = (self.hexa_pong_x + self.offset, self.hexa_pong_y)
                self.state = 'Hexa Pong'
            elif self.state == 'Tetra Pong':
                self.cursor_rect.midtop = (self.pong_x + self.offset, self.pong_y)
                self.state = 'Pong'
            elif self.state == 'Hexa Pong':
                self.cursor_rect.midtop = (self.tetra_pong_x + self.offset, self.tetra_pong_y)
                self.state = 'Tetra Pong'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Pong':
                self.game.playing = False
                self.game.playing_pong = True
                self.game.pong.run_game()
            elif self.state == 'Tetra Pong':
                self.game.playing_tetra_pong = True
            elif self.state == 'Hexa Pong':
                self.game.playing_hexa_pong = True
            self.run_game_menu_display = False


class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Volume'
        self.volx, self.voly = self.mid_w, self.mid_h + 20
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Options', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30)
            self.game.draw_text("Volume", 15, self.volx, self.voly)
            self.game.draw_text("Controls", 15, self.controlsx, self.controlsy)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Volume':
                self.state = 'Controls'
                self.cursor_rect.midtop = (self.controlsx + self.offset, self.controlsy)
            elif self.state == 'Controls':
                self.state = 'Volume'
                self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
        elif self.game.START_KEY:
            # TO-DO: Create a Volume Menu and a Controls Menu
            pass


class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Credits', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text('Made by me', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 10)
            self.blit_screen()
            
            
pygame.init()
try:
    font = pygame.font.Font("Assets/fonts/PRESSSTART2P-VAV7.TTF", 20)
except:
    print("Font file not found! Make sure 'PressStart2P-Regular.ttf' is in the Clouds 3 folder")
    font = pygame.font.SysFont('PressStart2P-Regular', 36)
         
class Button:
    def __init__(self, x, y, text):
        self.text = font.render(text, True, (240, 240, 240))
        self.rect = self.text.get_rect()
        self.rect.center = (x, y)
        
    def draw(self, surface):
        surface.blit(self.text, self.rect)
        
    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)           
            
class MenuSystem():
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN):
        self.screen_width = SCREEN_WIDTH
        self.screen_height = SCREEN_HEIGHT
        self.screen = SCREEN
        
    
    def Draw_BackGround(self):
        scroll = 0
        bg_images = []
        
        for i in range(1, 5):
            bg_image = pygame.image.load(f"{os.path.join(os.getcwd(),"Assets", "bg_images")}\\layer-{i}.png").convert_alpha()
            bg_images.append(bg_image)
        
        bg_width = self.bg_images[0].get_width()
        tiles = math.ceil(self.screen_width / bg_width) + 1
        layer_speeds = [0.2, 0, 0.6, 0.8]  # Moon (layer 2) has speed 0 to stay fixed
        
        for x in range(0, tiles + 1):
            pos_x = ((x * bg_width) - (scroll * layer_speeds[0])) % (bg_width * tiles)
            self.screen.blit(self.bg_images[0], (pos_x - bg_width, 0))
            
        moon_x = (self.screen_width - bg_images[1].get_width()) // 2
        self.screen.blit(bg_images[1], (moon_x, 0))
        
        for layer in [2, 3]:  # indices for layers 3 and 4
            for x in range(0, tiles + 1):
                pos_x = ((x * bg_width) - (self.scroll * layer_speeds[layer])) % (bg_width * tiles)
                self.screen.blit(bg_images[layer], (pos_x - bg_width, 0))
        
        
    def Draw_MainMenu(self):
        play_button = Button(self.screen_width // 2, self.screen_height // 2, "Play!")
        self.Draw_BackGround()
        play_button.draw(self.screen)
        self.scroll += 2
        