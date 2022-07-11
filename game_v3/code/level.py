import pygame, settings, tiles
from particles import *

class Level:
    def __init__(self, level_data, size):

        self.current_x = 0

        # level setup
        self.map_surface = pygame.Surface(size)
        self.map_rect = self.map_surface.get_rect()
        self.setupLevel(level_data)

        # dust
        self.dust_sprite = pygame.sprite.GroupSingle()
        self.player_on_ground = False

    def create_jump_particles(self, player):
        if player.facing_right:
            player.rect.center -= pygame.math.Vector2(10, 5)
        else:
            player.rect.center += pygame.math.Vector2(10, -5)
        jump_particle_sprite = ParticleEffect(player.rect.center, "jump")
        self.dust_sprite.add(jump_particle_sprite)
    
    def get_player_on_ground(self, player):
        if player.on_ground:
            self.player_on_ground = True
        else:
            self.player_on_ground = False
    
    def create_landing_dust(self, player):
        if not self.player_on_ground and player.on_ground and not self.dust_sprite.sprites():
            if player.facing_right:
                offset = pygame.math.Vector2(10, 15)
            else:
                offset = pygame.math.Vector2(-10, 15)
            fall_dust_particle = ParticleEffect(player.rect.midbottom - offset, "land")
            self.dust_sprite.add(fall_dust_particle)
    
    def setupLevel(self, layout):
        self.tiles = pygame.sprite.Group()

        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * settings.tile_size
                y = row_index * settings.tile_size

                if cell == "X":
                    tile = tiles.Block((settings.tile_size, settings.tile_size), x, y)
                    self.tiles.add(tile)