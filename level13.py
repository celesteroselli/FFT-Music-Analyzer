import pygame
from Fourier.player import *
from Fourier.music import *
from pygame import *
from Fourier.physics import *
from Fourier.camera import *
from Fourier.Level import Level

import numpy as np

foreground = []

game_map = "4_1"

num_of_elements = 6

factor = 6

def level13inputs(variables, events, player):
    foreground = variables["foreground"]
    camera = variables.get("camera")
    
    for x in foreground[0::2]:
        if type(x)==type(("1","1")):
            if (x[1].y == (player.rect.y+player.rect.h)) and (player.rect.x >= x[1].x) and (player.rect.x < (x[1].x + x[1].w)):
                print("KILLED")
                player.kill(camera)
                variables["killed"] = True
                
    #things that kill the player
    length = len(foreground)
    if (foreground[length-1].y == (player.rect.y+player.rect.h)) and (player.rect.x >= foreground[length-1].x) and (player.rect.x < (foreground[length-1].x + foreground[length-1].w)):
        print("KILLED")
        player.kill(camera)
        variables["killed"] = True
    
    if variables["killed"]==True:
        print("setting foreground back to original")
        variables["foreground"] = variables["original"]
        variables["killed"] = False
    
    foreground = variables.get("foreground")        
    
    for event in events:
        if event.type == pygame.MOUSEBUTTONUP:
            print("mouse button up in level1 copy")
        # Check if the left mouse button was pressed (button 1)
            if event.button == 1:
                # Get the mouse position at the time of the click
                mouse_pos = event.pos
                # Check if the mouse position collides with the rect
                new_pos = (mouse_pos[0] + camera.offset.x, mouse_pos[1] + camera.offset.y)
                for i in range(num_of_elements):
                    #i = 0 -> 0
                    #i = 1 -> 2
                    #i = 2 -> 4
                    #i = 3 -> 6
                    #i = 4 -> 8
                    #i = 5 -> 10
                    if (i*2) < (len(foreground)-1):
                        print(foreground[i*2][1])
                        if foreground[i*2][1].collidepoint(new_pos):
                            run = chord(variables["pitch_list"][i], "major")
                            print(run)
                            variables["figure"] = run[1]
                            variables["answer"] = run[2]
                            if run[0]:
                                variables["foreground"].insert((i*2)+1, (-4,(pygame.Rect(((TILE_SIZE*variables["posx"][i], TILE_SIZE*(variables["posy"][i]-1)), (TILE_SIZE*5, TILE_SIZE))))))
                                print(variables["foreground"])
                            else:
                                variables["wrong"] = run[2]
                    
                    
def level13setup(foreground, camera):
    temp_dict = {}
    
    temp_dict["killed"] = False
    temp_dict["congrats"] = False
    
    temp_dict["foreground"] = []
    temp_dict["camera"] = camera
    temp_dict["game_map"] = game_map
    temp_dict["running"] = True
    temp_dict["wrong"] = False
    
    temp_dict["pitch_list"] = ["C", "D", "E", "D", "C#", "E"]
    temp_dict["posx"] = [10, 21, 38, 55, 66, 89]
    temp_dict["posy"] = [16, 16, 15, 14, 14, 12]
    
    for i in range(len(temp_dict["posx"])):
        temp_dict["foreground"].append((-3, pygame.rect.Rect(TILE_SIZE*(temp_dict["posx"][i]), TILE_SIZE*(temp_dict["posy"][i]), TILE_SIZE*5, TILE_SIZE)))
        
    temp_dict["foreground"].append(pygame.rect.Rect(0, TILE_SIZE*19, TILE_SIZE*100, TILE_SIZE))
    
    temp_dict["original"] = temp_dict["foreground"].copy()
    
    return temp_dict

def level13dialogue(variables, player):
    if ((pygame.time.get_ticks() - variables["starttime"]) > 1200) and (variables["dialogue_count"]==0):
        variables["dialogue_on"] = True
        return "sing a major chord"
    
    if ((player.rect.x > 92*TILE_SIZE)):
        variables["dialogue_on"] = True
        variables["running"] = False
        return "congrats! you finished the level!"
    
    if (variables["wrong"] != False ):
        variables["dialogue_on"] = True
        return variables["wrong"]
    
    if (variables["figure"]):
        variables["dialogue_on"] = True
        return variables["answer"]

Level_13 = Level(foreground, game_map, level13inputs, level13setup, level13dialogue, "4", "")