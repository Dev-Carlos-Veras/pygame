import pygame, settings

import level, camera, player

class GameManager:
    def __init__(self):

        #main screen
        self.screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))

        #level
        self.level = level.Level(settings.level_map, (5120, 5120))

        #camera
        self.camera_group = camera.CameraGroup()

        #player
        self.player = player.Player(50, 196, self.camera_group, self.level, self.level.create_jump_particles)

        #world watcher
        self.world_watchers = set()
    
    def register_world_watcher(self, member):
        self.world_watchers.add(member)
    
    def unregister_world_watcher(self, member):
        self.world_watchers.remove(member)
    
    def dispatch(self, level_object):
        for watcher in self.world_watchers:

            watcher.level_obj = level_object
    
    def rungame(self):
        self.screen.fill(settings.bg_color)

        #dust particles
        self.level.dust_sprite.update(self.camera_group.offset)

        self.camera_group.update()
        self.camera_group.renderScreen(self.level, self.player)




#All subscribers must have an update() method