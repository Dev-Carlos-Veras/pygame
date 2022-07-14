import pygame

#Screen setup
screen_width = 1280
screen_height = 720

#Global variables
bg_color = pygame.Color("#0f070d")
accent_color = pygame.Color(152, 142, 230)
great_color = pygame.Color(245, 73, 60)

#Map setup
level_map = [
"                                                                   ",
"                                                                   ",
"                                                                   ",
"                                                                   ",
"                                                                   ",
"                                                                   ",
"                                                                   ",
"XXXXXXXXXXXXXXXXXXXXXXXXXX                     XXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXX                 XXXXXXXXXXXXXXXXXXXXXXXX",
"                                                                   ",
"                                                                   ",
"                                                                   ",
"                                  XXXXXXXXX                        ",
"                                                                   ",
"                                                                   ",
"                                                                   ",
"                 XXXXXXXXX                                         ",
"                                                                   ",
"                                                                   ",
"                                                                   ",
"XXXXXX                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"                                                                   ",
"                                                                   ",
"                                                                   ",
"           XXXXXXXXX                                               ",
"                                                                   ",
"                                                                   ",
"                                                                   ",
"XXXXXXXXXXXXXXXXXXXXXXXXXXX       XXXXXXXX                         ",
"                                                                   ",
"                                                                   ",
"                                                                   ",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXX                        X             ",
"                                                                   ",
"                                                                   ",
"                                                                   ",
"                               XXXXXXXXX              XXXXXXXXX    ",
"                                                                   ",
"                                                                   ",
"                                                                   ",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXX               XXXXXXXXXXXXXXXXXXXXXXXX",
"                                                                   ",
"                                                                   ",
"                                                                   ",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX            XXXXXXXXXXXX",
"                                                                   ",
"                                                                   ",
"                                                    X              ",
"                                                                   ",
"                                                                   ",
"                                         XXXXXXXXX                 ",
"                                                                   ",
"                                                                   ",
"                                                         XXXXXXX   ",
"                                                                   ",
"X                  X   X                                           ",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
]
tile_size = 32