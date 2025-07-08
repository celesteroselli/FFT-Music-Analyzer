# Simple pygame program

# Import and initialize the pygame library
import pygame
from Fourier.player import *
from Fourier.music import *
from pygame import *
from Fourier.physics import *
from Fourier.camera import *
from Fourier.dialogue import dialogue_actions

def level_run(current_level, events, camera, m_player, follow):
    
    if (not current_level.variables["dialogue_on"]):
        #freezes screen if dialogue!
        handle_move(m_player)
        draw_background(camera, m_player, current_level.variables["foreground"], current_level.variables["game_map"], current_level.variables["background"], current_level.variables["game_back"], current_level.variables["game_front"])
        m_player.draw(display, camera)
        follow.scroll()
    else:
        if (current_level.variables["new_dialogue"]):
            #handling dialogue display stuff
            print("writing text")
            pygame.draw.rect(display, color3, current_level.variables["dialogue_box"])
            text_surface = my_font.render(current_level.variables["write"], False, color1, None)
            display.blit(text_surface,(current_level.variables["dialogue_box"].x,current_level.variables["dialogue_box"].y))
            current_level.variables["new_dialogue"] = False
            if current_level.variables["figure"] != False:
                display.blit(current_level.variables["figure"], (500,100))

    current_level.variables["write"] = current_level.dialogue(m_player)
            
    current_level.inputs(events, m_player)    

    for event in events:
            
        if ((event.type == pygame.KEYDOWN) and (current_level.variables["dialogue_on"]==True)):
            if event.key == pygame.K_ESCAPE: 
                print("pressed escape")
                current_level.variables["dialogue_on"] = False
                current_level.variables["new_dialogue"] = True
                current_level.variables["dialogue_count"] += 1
                current_level.variables["wrong"] = False
                current_level.variables["figure"] = False
                
        if (event.type==KEYDOWN) and (event.key == pygame.K_q):
            print("q pressed")
            current_level.variables["running"] = False     

        if current_level.variables["running"]==False:
                    return False
            
    pygame.display.update()
    return display