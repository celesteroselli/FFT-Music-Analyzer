import os

import pygame
from Fourier.LevelManager import *
from Fourier.physics import screen
from Fourier.level1 import Level_1
from Fourier.lesson import *
from Fourier.usersettings import *
from pygame_markdown import MarkdownRenderer
from Fourier.LevelPicker import pick
import gif_pygame

def main():
    
    types = {
    1: ("high", 1),
    2: ("med", 0.5),
    3: ("low", 0.25)
}
    e = 1
    
    pygame.init()

    music = pygame.mixer.music.load(resource_path("statics/audio_final.mp3"))
    pygame.mixer.music.play(loops=-1)

    running = True

    startx = PLAYER_SCREEN_OFFSET
    starty = 1600
    m_player = PlayerClass(startx, starty, 150, 150)
    camera = Camera(m_player)
    follow = CamScroll(camera, m_player)

    #give a base case just in case
    current_level = Level_1

    clock = pygame.time.Clock()

    current_lesson = lesson_content(1, 1, 0)
    lesson_first = True
    isdone = MutableInt(0)

    is_level = False
    change_octave(types.get(e)[1])

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
                    screen.blit(do_lesson(current_lesson[1], current_lesson[0], pygame_events, mouse_x, mouse_y, mouse_pressed, current_lesson[5]), (0,0))
                    inputs(pygame_events, current_lesson[0], current_lesson[2], isdone, current_lesson[3], current_lesson[4])
                else:
                    isdone.increment(-1)
                    pygame.time.delay(150)
                    startTime = pygame.time.get_ticks()
                    lesson_first=False
                    current_level.setup(camera, startTime)
                    m_player.rect.x = startx
                    m_player.rect.y = starty
            else:
            #what should you run after the lesson
                pygame.mixer.music.pause()
                run = level_run(current_level, pygame_events, camera, m_player, follow)
                if run != False:
                    screen.blit(run, (0,0))
                else:
                    time.sleep(0.5)
                    is_level = False
                    lesson_first = True
        else:
        #else, show the level screen
            pygame.mixer.music.unpause()
            run = pick(pygame_events)
            if run[0] == True:
                #no level picked
                screen.blit(run[1], (0,0))
                octavetext = my_font.render("press e to change octaves:", False, color2, None)
                
                typetext = my_font.render(types.get(e)[0], False, color2, None)
                
                screen.blit(octavetext, (20, octavetext.get_height()+20))
                screen.blit(typetext, (20+(octavetext.get_width()-typetext.get_width())/2, octavetext.get_height()*2+40))
                
                for event in pygame_events:
                    if (event.type==KEYDOWN) and (event.key == pygame.K_e):
                        if e<3:
                            e = e+1
                            change_octave(types.get(e)[1])
                        else:
                            e=1
                            change_octave(types.get(e)[1])
            else:
                current_level = run[1]
                unit, level = run[2][0], run[2][1]
                if (unit==1 and level==1):
                    is_gif = 0
                elif (unit==4 and level==2) or (unit==2 and (level==2 or level==3 or level==4)):
                    is_gif = -1
                else:
                    is_gif=1
                current_lesson = lesson_content(unit, level, is_gif)
                is_level = True
    
        clock.tick(110)
    
    pygame.quit()
    
if __name__ == "__main__":
    main()