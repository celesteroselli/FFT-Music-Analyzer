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

num_of_elements = 9

factor = 4

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
        (pygame.Rect((((TILE_SIZE*57), (TILE_SIZE*14)+(100)-(variables["y5_height"]*factor)), (300, 50)))),
        (pygame.Rect((((TILE_SIZE*67), (TILE_SIZE*16)+(100)-(variables["y6_height"]*factor)), (300, 50)))),
        (pygame.Rect((((TILE_SIZE*73), (TILE_SIZE*14)+(100)-(variables["y7_height"]*factor)), (300, 50)))),
        (pygame.Rect((((TILE_SIZE*80), (TILE_SIZE*11)+(100)-(variables["y8_height"]*factor)), (300, 50)))),
        (pygame.Rect((((TILE_SIZE*88), (TILE_SIZE*14)+(100)-(variables["y9_height"]*factor)), (300, 50)))),
        (pygame.Rect((((TILE_SIZE*79), (TILE_SIZE*13), (600, 50))))),
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
    temp_dict["y2"] = 530 * OCTAVE
    temp_dict["y3"] = 600 * OCTAVE
    temp_dict["y4"] = 440 * OCTAVE
    temp_dict["y5"] = 390 * OCTAVE
    temp_dict["y6"] = 440 * OCTAVE
    temp_dict["y7"] = 600 * OCTAVE
    temp_dict["y8"] = 530 * OCTAVE
    temp_dict["y9"] = 500 * OCTAVE
    
    for i in range(num_of_elements):
    
        temp_dict[f"y{i+1}_height"] = temp_dict[f"y{i+1}"] - temp_dict.get("lowest")
        temp_dict[f"y{i+1}_height_goal"] = temp_dict[f"y{i+1}"] - temp_dict.get("lowest")
    
        temp_dict["foreground"] = foreground
        temp_dict["camera"] = camera
        temp_dict["running"] = True
        temp_dict["game_map"] = game_map
    
    return temp_dict

def level1dialogue(variables, player):
    print(player.rect.x)
    print(variables["dialogue_count"])
    if ((pygame.time.get_ticks() - variables["starttime"]) > 1200) and (variables["dialogue_count"]==0):
        variables["dialogue_on"] = True
        return "you feel a need to escape"
    
    if ((player.rect.x > 4*TILE_SIZE) and (variables["dialogue_count"]==1)):
        variables["dialogue_on"] = True
        return "stand on the platform and click it"
    
    if ((player.rect.x > 8*TILE_SIZE) and (variables["dialogue_count"]==2)):
        variables["dialogue_on"] = True
        return "higher pitches move the platform higher, lower pitches move it lower"
    
    if ((player.rect.x > 77*TILE_SIZE) and (variables["dialogue_count"]==3)):
        variables["dialogue_on"] = True
        return "better sing the right pitch to avoid the ceiling and thorns"
    #79, 13

Level_1 = Level(foreground, game_map, level1inputs, level1setup, level1dialogue)