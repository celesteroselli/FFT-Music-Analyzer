import pygame
from player import *
from music import *
from pygame import *
from physics import *
from camera import *
from Level import Level

import numpy as np

foreground = []

game_map = "4_1"

num_of_elements = 1

factor = 6

foreground = [
        #x-left = x tiles from left
        #y-top = y-1 tiles from top
        (-3, (pygame.Rect((((TILE_SIZE*10), (TILE_SIZE*16))), (TILE_SIZE*5, TILE_SIZE)))),
        
        (pygame.Rect((((TILE_SIZE*0), (TILE_SIZE*19))), (TILE_SIZE*100, TILE_SIZE*1))),
]

def level13inputs(variables, events, player):
    
    camera = variables.get("camera")
    foreground = variables.get("foreground")
    
    if variables["killed"]==True:
        pass
                
    #things that kill the player
    if (foreground[len(foreground)-1].y == (player.rect.y+player.rect.h)) and (player.rect.x >= foreground[i].x) and (player.rect.x < (foreground[i].x + foreground[i].w)):
        print("KILLED")
        player.kill(camera)
        variables["killed"] = True
    
    variables["foreground"] = foreground
            
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
                    if foreground[i][1].collidepoint(new_pos):
                        run = chord("C")
                        print(run)
                        variables["figure"] = run[1]
                        variables["answer"] = run[2]
                        if run[0]:
                            variables["foreground"].insert(len(variables["foreground"])-1, (-4,(pygame.Rect(((TILE_SIZE*10, TILE_SIZE*15), (TILE_SIZE*5, TILE_SIZE))))))
                            print(variables["foreground"])
                        else:
                            variables["wrong"] = run[2]
                    
def level13setup(foreground, camera):
    temp_dict = {}
    
    temp_dict["killed"] = False
    temp_dict["congrats"] = False
    
    temp_dict["foreground"] = foreground
    temp_dict["camera"] = camera
    temp_dict["game_map"] = game_map
    temp_dict["running"] = True
    temp_dict["wrong"] = False
    
    return temp_dict

def level13dialogue(variables, player):
    if ((pygame.time.get_ticks() - variables["starttime"]) > 1200) and (variables["dialogue_count"]==0):
        variables["dialogue_on"] = True
        return "you feel a need to escape"
    
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