import pygame

class menu:
    def __init__(self):
        
        self.background = pygame.image.load("/home/carlitos/Projects/Pygame/game_v3/graphics/menu/menu_wallpaper.jpeg").convert()
        self.background_rect = self.background.get_rect()