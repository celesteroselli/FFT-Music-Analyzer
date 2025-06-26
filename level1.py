import pygame
from player import *
from music import *
from pygame import *
from physics import *
from camera import *
from Level import Level

import numpy as np

foreground = []

game_map = "1_1"

def level1inputs(variables, events, player):
    global y
    
    global camera
    camera = variables.get("camera")
    global foreground
    foreground = variables.get("foreground")
    
    y = variables.get("y")
    y_height = variables.get("y_height")
    
    global running
    running = variables.get("running")
    
    foreground = [
        #x-left = x tiles from left
        #y-top = y-1 tiles from top
        (pygame.Rect((((TILE_SIZE*9), (TILE_SIZE*16)+(100)-(y_height*1.7)), (300, 50)))),
    ]
    
    if np.absolute(variables["y_height_goal"]-variables["y_height"]) > 10:
        if variables["y_height_goal"] > variables["y_height"]:
            variables["y_height"] += 1
        elif variables["y_height_goal"] < variables["y_height"]:
            variables["y_height"] -= 1
    
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
                if foreground[0].collidepoint(new_pos):
                    if (foreground[0].y == (player.rect.y+player.rect.h)) and (player.rect.x >= foreground[0].x) and (player.rect.x < (foreground[0].x + foreground[0].w)):
                        print("player is touching rectangle so moving it")
                        variables["y"] = pitch(y)
                        variables["y_height_goal"] = variables["y"] - variables["lowest"]
                    else:
                        print("player not colliding")
                    
def level1setup(foreground, camera):
    temp_dict = {}
    
    temp_dict["lowest"] = 440 * OCTAVE

    temp_dict["y"] = 440 * OCTAVE
    temp_dict["y_height"] = temp_dict["y"] - temp_dict.get("lowest")
    temp_dict["y_height_goal"] = temp_dict["y"] - temp_dict.get("lowest")
    
    temp_dict["foreground"] = foreground
    temp_dict["camera"] = camera
    temp_dict["running"] = True
    temp_dict["game_map"] = game_map
    
    return temp_dict

def level1dialogue(variables):
    if ((pygame.time.get_ticks() - variables["starttime"]) > 3000) and (variables["dialogue_count"]==0):
        variables["dialogue_on"] = True
        return "oh hey"

Level_1 = Level(foreground, game_map, level1inputs, level1setup, level1dialogue)