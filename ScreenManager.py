import pygame
from LevelManager import *
from physics import screen
from level1 import Level_1
from usersettings import *

pygame.init()

running = True
m_player = PlayerClass(PLAYER_SCREEN_OFFSET, 10, 100, 100)
camera = Camera(m_player)
follow = CamScroll(camera, m_player)

current_level = Level_1
current_level.setup(camera)

clock = pygame.time.Clock()

while running:
    screen.blit(level_run(current_level, pygame.event.get(), camera, m_player, follow), (0,0))
    level_first = False
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
            
    clock.tick(80)
pygame.quit()