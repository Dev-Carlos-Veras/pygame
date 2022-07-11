import pygame, settings

class Block(pygame.sprite.Sprite):
    def __init__(self, size, pos_x, pos_y):
        super().__init__()
        self.image = pygame.Surface(size)
        self.image.fill(settings.accent_color)
        self.rect = self.image.get_rect( topleft = (pos_x, pos_y))