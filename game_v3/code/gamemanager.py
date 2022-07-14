import pygame, settings

import level, camera, player

from level_data import *

class GameManager:
    def __init__(self):

        #main screen
        self.screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))

        #level
        self.level = level.Level(level_1, (2912, 2912))

        #camera
        self.camera_group = camera.CameraGroup()

        #player
        self.player = player.Player(self.level.spawn_x, self.level.spawn_y, self.camera_group, self.level, self.level.create_jump_particles)
    
    def rungame(self):
        self.screen.fill(settings.bg_color)

        #dust particles
        self.level.dust_sprite.update(self.camera_group.offset)

        self.camera_group.update()
        self.camera_group.renderScreen(self.level, self.player)




#All subscribers must have an update() method