import pygame
from Fourier.player import *
from Fourier.music import *
from pygame import *
from Fourier.physics import *
from Fourier.camera import *
from Fourier.Level import Level

import numpy as np

foreground = [
        #x-left = x tiles from left
        #y-top = y-1 tiles from top
        (pygame.Rect((((0), (TILE_SIZE*20)), (TILE_SIZE*100, 50)))),
        (pygame.Rect((((TILE_SIZE*9), (TILE_SIZE*15)), (300, 50)))),
]

game_map = "1_3"

def level3inputs(variables, events, player):
    
    camera = variables.get("camera")
    foreground = variables.get("foreground")
    
    num_of_elements = 9
    
    if variables["killed"]==True:
        variables["killed"]=False
    
    foreground_list = [
        #x-left = x tiles from left
        #y-top = y-1 tiles from top
        (pygame.Rect((((TILE_SIZE*14), (TILE_SIZE*15)), (300, 100)))),
        (pygame.Rect((((TILE_SIZE*21), (TILE_SIZE*15)), (300, 100)))),
        (pygame.Rect((((TILE_SIZE*28), (TILE_SIZE*15)), (300, 100)))),
        (pygame.Rect((((TILE_SIZE*55), (TILE_SIZE*12)), (300, 100)))),
        (pygame.Rect((((TILE_SIZE*62), (TILE_SIZE*12)), (300, 100)))),
        (pygame.Rect((((TILE_SIZE*69), (TILE_SIZE*12)), (300, 100)))),
        (pygame.Rect((((TILE_SIZE*76), (TILE_SIZE*10)), (300, 100)))),
        #extra one at end with no keyboard on top
        (pygame.Rect((((TILE_SIZE*88), (TILE_SIZE*11)), (300, 100)))),
    ]
    
    pitch_list = [
        #C
        261.63*2*get_octave(),
        #D
        293.66*2*get_octave(),
        #A
        440*2*get_octave(),
        #F
        349.23*2*get_octave(),
        #G#
        415.30*2*get_octave(),
        #E
        329.63*2*get_octave(),
        #A
        440*2*get_octave(),
        #B
        493.88*2*get_octave(),
    ]
    
    background = [
        (1,(pygame.Rect((((TILE_SIZE*9), (TILE_SIZE*15.8)), (300, 300))))),
        (2, (pygame.Rect((((TILE_SIZE*14), (TILE_SIZE*15.8)), (300, 300))))),
        (3, (pygame.Rect((((TILE_SIZE*21), (TILE_SIZE*15.8)), (300, 300))))),
        (4,(pygame.Rect((((TILE_SIZE*28), (TILE_SIZE*15.8)), (300, 300))))),
        (7,(pygame.Rect((((TILE_SIZE*55), (TILE_SIZE*12.8)), (300, 300))))),
        (5,(pygame.Rect((((TILE_SIZE*62), (TILE_SIZE*12.8)), (300, 300))))),
        (3, (pygame.Rect((((TILE_SIZE*69), (TILE_SIZE*12.8)), (300, 300))))),
        (6, (pygame.Rect((((TILE_SIZE*76), (TILE_SIZE*10.8)), (300, 300))))),
    ]
                
    #things that kill the player
    for i in [0]:
        if (foreground[i].y == (player.rect.y+player.rect.h)) and (player.rect.x >= foreground[i].x) and (player.rect.x < (foreground[i].x + foreground[i].w)):
            print("KILLED")
            player.kill(camera)
            variables["foreground"] = [
            #x-left = x tiles from left
            #y-top = y-1 tiles from top
            (pygame.Rect((((0), (TILE_SIZE*20)), (TILE_SIZE*100, 50)))),
            (pygame.Rect((((TILE_SIZE*9), (TILE_SIZE*15)), (300, 50)))),
            ]
            variables["killed"] = True
            
    for event in events:
        if event.type == pygame.MOUSEBUTTONUP:
            print("mouse button up in level1 copy")
        # Check if the left mouse button was pressed (button 1)
            if event.button == 1:
                # Get the mouse position at the time of the click
                mouse_pos = event.pos
                # Check if the mouse position collides with the rect
                new_pos = (mouse_pos[0] + camera.offset.x, mouse_pos[1] + camera.offset.y)
                for i in range(len(background)):
                    print(background[i][1])
                    if background[i][1].collidepoint(new_pos):
                        print(f"hitting background {i}")
                        run = harmonize(pitch_list[i], 1)
                        variables["figure"] = run[2]
                        variables["last_note"] = pitch_list[i]
                        if run[0]:
                            foreground.append(foreground_list[i])
                        else:
                            variables["wrong"] = run[3]
    
    variables["background"] = background
    variables["foreground"] = foreground
                    
def level3setup(foreground, camera):
    temp_dict = {}
    
    temp_dict["killed"] = False
    temp_dict["congrats"] = False
    
    temp_dict["foreground"] = foreground
    temp_dict["camera"] = camera
    temp_dict["game_map"] = game_map
    temp_dict["running"] = True
    temp_dict["last_note"] = 400
    
    return temp_dict

def level3dialogue(variables, player):
    if ((pygame.time.get_ticks() - variables["starttime"]) > 1200) and (variables["dialogue_count"]==0):
        variables["dialogue_on"] = True
        return "match the pitches"
    
    if (variables["wrong"] != False ):
        variables["dialogue_on"] = True
        return variables["wrong"]
    
    if ((player.rect.x > 93*TILE_SIZE)):
        variables["dialogue_on"] = True
        variables["running"] = False
        return "congrats! you finished the level!"
    
    if (variables["figure"]):
        variables["dialogue_on"] = True
        return f"you sang {variables["last_note"]} hz"

Level_3 = Level(foreground, game_map, level3inputs, level3setup, level3dialogue, "1", "1fg")