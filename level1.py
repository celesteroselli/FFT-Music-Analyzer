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

num_of_elements = 4

factor = 3

def level1inputs(variables, events, player):
    
    camera = variables.get("camera")
    foreground = variables.get("foreground")
    
    global running
    running = variables.get("running")
    
    foreground = [
        #x-left = x tiles from left
        #y-top = y-1 tiles from top
        (pygame.Rect((((TILE_SIZE*9), (TILE_SIZE*16)+(100)-(variables["y1_height"]*factor)), (300, 50)))),
        (pygame.Rect((((TILE_SIZE*16), (TILE_SIZE*14)+(100)-(variables["y2_height"]*factor)), (300, 50)))),
        (pygame.Rect((((TILE_SIZE*23), (TILE_SIZE*11)+(100)-(variables["y3_height"]*factor)), (300, 50)))),
        (pygame.Rect((((TILE_SIZE*41), (TILE_SIZE*16)+(100)-(variables["y4_height"]*factor)), (300, 50)))),
    ]
    
    for i in range(num_of_elements):
        if np.absolute(variables[f"y{i+1}_height_goal"]-variables[f"y{i+1}_height"]) > 10:
            if variables[f"y{i+1}_height_goal"] > variables[f"y{i+1}_height"]:
                variables[f"y{i+1}_height"] += 1
            elif variables[f"y{i+1}_height_goal"] < variables[f"y{i+1}_height"]:
                variables[f"y{i+1}_height"] -= 1

    
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
                    if foreground[i].collidepoint(new_pos):
                        if (foreground[i].y == (player.rect.y+player.rect.h)) and (player.rect.x >= foreground[i].x) and (player.rect.x < (foreground[i].x + foreground[i].w)):
                            print("player is touching rectangle so moving it")
                            variables[f"y{i+1}"] = pitch(variables[f"y{i+1}"])
                            variables[f"y{i+1}_height_goal"] = variables[f"y{i+1}"] - variables["lowest"]
                        else:
                            print("player not colliding")
                    
def level1setup(foreground, camera):
    temp_dict = {}
    
    temp_dict["lowest"] = 440 * OCTAVE
    
    temp_dict["y1"] = 440 * OCTAVE
    temp_dict["y2"] = 500 * OCTAVE
    temp_dict["y3"] = 480 * OCTAVE
    temp_dict["y4"] = 440 * OCTAVE
    
    for i in range(num_of_elements):
    
        temp_dict[f"y{i+1}_height"] = temp_dict[f"y{i+1}"] - temp_dict.get("lowest")
        temp_dict[f"y{i+1}_height_goal"] = temp_dict[f"y{i+1}"] - temp_dict.get("lowest")
    
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