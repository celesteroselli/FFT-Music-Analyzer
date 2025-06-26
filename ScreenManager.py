import pygame
from LevelManager import *
from physics import screen
from level1 import Level_1
from lesson import *
from usersettings import *
from pygame_markdown import MarkdownRenderer

pygame.init()

running = True
m_player = PlayerClass(PLAYER_SCREEN_OFFSET, 2000, 100, 100)
camera = Camera(m_player)
follow = CamScroll(camera, m_player)

current_level = Level_1

clock = pygame.time.Clock()

current_lesson = lesson_content(1, 1)
lesson_first = True
isdone = MutableInt(0)

while running:
    pygame_events = pygame.event.get()
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()
    
    for event in pygame_events:
        if event.type == pygame.QUIT:
            running = False
    
    #do the lesson first!
    if lesson_first:
        if(isdone.value==0):
            screen.blit(do_lesson(current_lesson[1], current_lesson[0], pygame_events, mouse_x, mouse_y, mouse_pressed), (0,0))
            inputs(pygame_events, current_lesson[0], current_lesson[2], isdone, current_lesson[3], current_lesson[4])
        else:
            pygame.time.delay(150)
            startTime = pygame.time.get_ticks()
            lesson_first=False
            current_level.setup(camera, startTime)
    else:
    #what should you run after the lesson
        screen.blit(level_run(current_level, pygame_events, camera, m_player, follow), (0,0))
    
            
    clock.tick(90)
pygame.quit()