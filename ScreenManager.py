import pygame
from LevelManager import *
from physics import screen
from level1 import Level_1
from level2 import Level_2
from level3 import Level_3
from level4 import Level_4
from lesson import *
from usersettings import *
from pygame_markdown import MarkdownRenderer
from LevelPicker import pick

pygame.init()

running = True

startx = PLAYER_SCREEN_OFFSET
starty = 2000
m_player = PlayerClass(startx, starty, 100, 100)
camera = Camera(m_player)
follow = CamScroll(camera, m_player)

current_level = Level_2

clock = pygame.time.Clock()

current_lesson = lesson_content(1, 4)
lesson_first = True
isdone = MutableInt(0)

is_level = False

while running:
    pygame_events = pygame.event.get()
    for event in pygame_events:
            if event.type == pygame.QUIT:
                running = False
                
    #if the user is in a level, do the following each tick:
    if is_level:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
    
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
                m_player.rect.x = startx
                m_player.rect.y = starty
        else:
        #what should you run after the lesson
            run = level_run(current_level, pygame_events, camera, m_player, follow)
            if run != False:
                screen.blit(run, (0,0))
            else:
                time.sleep(0.5)
                is_level = False
                lesson_first = True
    else:
    #else, show the level screen
        run = pick(pygame_events)
        if run[0] == True:
            screen.blit(run[1], (0,0))
        else:
            current_level = run[1]
            print("unit/level:")
            print(run[2][0])
            print(run[2][1])
            current_lesson = lesson_content(run[2][0], run[2][1])
            is_level = True
    
    clock.tick(90)
    
pygame.quit()

def run_a_level():
    pass