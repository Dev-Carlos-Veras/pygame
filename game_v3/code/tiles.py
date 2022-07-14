import pygame, settings
from support import *

class Block(pygame.sprite.Sprite):
    def __init__(self, size, pos_x, pos_y):
        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill(settings.accent_color)
        self.rect = self.image.get_rect( topleft = (pos_x, pos_y))

class StaticBlock(Block):
    def __init__(self, size, pos_x, pos_y, surface):
        super().__init__(size, pos_x, pos_y)
        self.image = surface

class Soul(StaticBlock):
    def __init__(self, size, pos_x, pos_y):
        super().__init__(size, pos_x, pos_y, pygame.image.load("/home/carlitos/Projects/Pygame/game_v3/graphics/souls/bottle of soul.png").convert_alpha())
        offsety = pos_y + size[1]
        self.rect = self.image.get_rect( bottomleft = (pos_x, offsety))

class AnimatedBlock(Block):
    def __init__(self, size, pos_x, pos_y, path):
        super().__init__(size, pos_x, pos_y)
        self.frames = import_folder(path)
        self.frame_index = 0
        self.image = self.frames[self.frame_index]

    def animate(self):
        self.frame_index += 0.15
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]
    

