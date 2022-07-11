import pygame, sys

import gamemanager as gm

#General setup
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("pygame")

#gamemanager
gamemanager = gm.GameManager()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #Game
    gamemanager.rungame()

    #Setting
    pygame.display.flip()
    clock.tick(60)