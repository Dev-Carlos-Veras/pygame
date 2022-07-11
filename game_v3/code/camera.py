import pygame, settings

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()

        # Camera offset
        self.offset = pygame.math.Vector2(0, 0)
        self.half_w = self.display_surface.get_size()[0] // 2
        self.half_h = self.display_surface.get_size()[1] // 2

    def center_camera_target(self, target):
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_h
    
    def renderScreen(self, level, player):

        # Camera func
        self.center_camera_target(player)

        self.display_surface.fill(settings.bg_color)

        # Ground
        ground_offset = level.map_rect.topleft - self.offset
        self.display_surface.blit(level.map_surface, ground_offset)
        level.map_surface.fill(settings.bg_color)
        level.tiles.draw(level.map_surface)

        # Particles
        #level.get_player_on_ground(player)
        #level.create_jump_particles(player)
        #level.create_landing_dust(player)
        #level.dust_sprite.draw(self.display_surface)

        # Active elements
        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset - (36, 24)
            self.display_surface.blit(sprite.image, offset_pos)