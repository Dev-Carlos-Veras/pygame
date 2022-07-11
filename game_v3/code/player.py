import pygame
from support import import_folder

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, group, level, create_jump_particles):
        super().__init__(group)
        self.player_surface = pygame.Surface((24, 68))
        self.import_character_assets()
        self.frame_index = 0
        self.animation_spd = 0.15
        self.image = self.animations["idle"][self.frame_index]
        self.rect = self.player_surface.get_rect( topleft = (pos_x, pos_y))

        # World awareness
        self.level_obj = level

        self.world_tiles = self.level_obj.tiles.sprites()

        # Dust particles
        self.import_dust_run_particles()
        self.dust_frame_index = 0
        self.dust_animation_spd = 0.15
        self.display_suface = self.level_obj.map_surface
        self.create_jump_particles = create_jump_particles

        # World constants
        self.gravity = 0.6

        # Player movement
        self.direction = pygame.math.Vector2(0, 0)
        self.hspd = 10
        self.vspd = -16

        # Player combat atributes
        self.max_health = 5
        self.actual_health = self.max_health

        # Player Status
        self.status = "idle"
        self.on_ground = False
        self.on_ceiling = False
        self.facing_right = True
        self.on_right = False
        self.on_left = False

    def import_character_assets(self):
        character_path = "../graphics/character/"
        self.animations = {"idle": [], "run": [], "jump": [], "fall": []}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)
    
    def import_dust_run_particles(self):
        self.dust_run_particles = import_folder("../graphics/character/dust_particles/run")

    def animate(self):
        animation = self.animations[self.status]

        # loop over frame index
        self.frame_index += self.animation_spd
        if self.frame_index >= len(animation):
            self.frame_index = 0
        
        image = animation[int(self.frame_index)]
        if self.facing_right:
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image, True, False)
            self.image = flipped_image
    
    def run_dust_animation(self):
        if self.status == "run" and self.on_ground:
            self.dust_frame_index += self.dust_animation_spd
            if self.dust_frame_index >= len(self.dust_run_particles):
                self.dust_frame_index = 0
            dust_particle = self.dust_run_particles[int(self.dust_frame_index)]

            if self.facing_right:
                pos = self.rect.bottomleft - pygame.math.Vector2(6, 10)
                self.display_suface.blit(dust_particle, pos)
            else:
                pos = self.rect.bottomright - pygame.math.Vector2(6, 10)
                flipped_dust_particle = pygame.transform.flip(dust_particle, True, False)
                self.display_suface.blit(flipped_dust_particle, pos)

    def keyPressed(self, keysPressed, inputKey):
        if keysPressed[inputKey]:
            return True
        else:
            return False

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.facing_right = True
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.facing_right = False
        else:
            self.direction.x = 0
        
        if self.keyPressed(keys, pygame.K_z) and self.on_ground:
            self.jump()
        elif not self.keyPressed(keys, pygame.K_z) and (not self.on_ceiling) and self.direction.y < 0:
            self.end_jump()
    
    def get_status(self):
        if self.direction.y < 0:
            self.status = "jump"
        elif self.direction.y > 1:
            self.status = "fall"
        else:
            if self.direction.x != 0:
                self.status = "run"
            else:
                self.status = "idle"

    def jump(self):
        self.direction.y = self.vspd
    
    def end_jump(self):
        self.direction.y = 0

    def applyGravity(self):
        self.direction.y += self.gravity
        self.rect.centery += self.direction.y
    
    def horizontal_collision(self):
        self.rect.centerx += self.direction.x * self.hspd

        for sprite in self.world_tiles:
            if sprite.rect.colliderect(self.rect):
                if self.direction.x > 0:
                    self.rect.right = sprite.rect.left
                    self.on_right = True
                    self.level_obj.current_x = self.rect.right
                
                elif self.direction.x < 0:
                    self.rect.left = sprite.rect.right
                    self.on_left = True
        
        if self.on_right and (self.rect.right > self.level_obj.current_x or self.direction. x <= 0):
            self.on_right = False
        if self.on_left and (self.rect.left < self.level_obj.current_x or self.direction.x >= 0):
            self.on_left = False

    def vertical_collision(self):
        
        self.applyGravity()

        for sprite in self.world_tiles:
            if sprite.rect.colliderect(self.rect):
                if self.direction.y > 0:
                    self.rect.bottom = sprite.rect.top
                    self.direction.y = 0
                    self.on_ground = True
                elif self.direction.y < 0:
                    self.rect.top = sprite.rect.bottom
                    self.direction.y = 0
                    self.on_ceiling = True
        
        if self.on_ground and self.direction.y < 0 or self.direction.y > 1:
            self.on_ground = False
        if self.on_ceiling and self.direction.y > 0.1:
            self.on_ceiling = False

    def update(self):
        self.input()

        self.get_status()
        self.animate()
        self.run_dust_animation()

        self.horizontal_collision()
        self.vertical_collision()