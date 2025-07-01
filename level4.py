import pygame
from player import *
from music import *
from pygame import *
from physics import *
from camera import *
from Level import Level

import numpy as np

foreground = []

game_map = "1_4"

num_of_elements = 9

factor = 4

def level4inputs(variables, events, player):
    
    camera = variables.get("camera")
    foreground = variables.get("foreground")
    
    if variables["killed"]==True:
        for i in range(num_of_elements):
            variables[f"y{i+1}_height"] = 0
    
    foreground = [
        #x-left = x tiles from left
        #y-top = y-1 tiles from top
        (pygame.Rect((((TILE_SIZE*15), (TILE_SIZE*16)+(100)-(variables["y1_height"]*factor)), (300, 50)))),
        (pygame.Rect((((TILE_SIZE*18), (TILE_SIZE*11)+(100)-(variables["y2_height"]*factor)), (300, 50)))),
        (pygame.Rect((((TILE_SIZE*35), (TILE_SIZE*14)+(100)-(variables["y3_height"]*factor)), (300, 50)))),
        (pygame.Rect((((TILE_SIZE*38), (TILE_SIZE*9)+(100)-(variables["y4_height"]*factor)), (300, 50)))),
        (pygame.Rect((((TILE_SIZE*51), (TILE_SIZE*15)+(100)-(variables["y5_height"]*factor)), (300, 50)))),
        (pygame.Rect((((TILE_SIZE*54), (TILE_SIZE*10)+(100)-(variables["y6_height"]*factor)), (300, 50)))),
        (pygame.Rect((((TILE_SIZE*75), (TILE_SIZE*12)+(100)-(variables["y7_height"]*factor)), (300, 50)))),
        (pygame.Rect((((TILE_SIZE*78), (TILE_SIZE*7)+(100)-(variables["y8_height"]*factor)), (300, 50)))),
        (pygame.Rect((((TILE_SIZE*87), (TILE_SIZE*12)+(100)-(variables["y9_height"]*factor)), (300, 50)))),
        (pygame.Rect((((0), (TILE_SIZE*20)), (TILE_SIZE*100, 50)))),
    ]
    
    for i in range(num_of_elements):
        if np.absolute(variables[f"y{i+1}_height_goal"]-variables[f"y{i+1}_height"]) > 10:
            if variables[f"y{i+1}_height_goal"] > variables[f"y{i+1}_height"]:
                variables[f"y{i+1}_height"] += 1
            elif variables[f"y{i+1}_height_goal"] < variables[f"y{i+1}_height"]:
                variables[f"y{i+1}_height"] -= 1
                
    #things that kill the player
    for i in [9]:
        if (foreground[i].y == (player.rect.y+player.rect.h)) and (player.rect.x >= foreground[i].x) and (player.rect.x < (foreground[i].x + foreground[i].w)):
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
                    if foreground[i].collidepoint(new_pos):
                        if variables[f"y{i+1}"] < (440*OCTAVE):
                            run = harmonize(variables[f"y{i+1}"], 2)
                            ifup = 2
                        else:
                            run = harmonize(variables[f"y{i+1}"], 0.5)
                            ifup = -2
                        orig = variables[f"orig_y{i+1}"]
                        if (run[0]==True):
                            variables[f"y{i+1}"] = run[1]
                            variables[f"y{i+1}_height_goal"] = ifup * 98
                            if (foreground[i].y == (player.rect.y+player.rect.h)) and (player.rect.x >= foreground[i].x) and (player.rect.x < (foreground[i].x + foreground[i].w)):
                                print("player is touching rectangle")
                            else:
                                print("player not colliding")
                        else:
                            variables["wrong"] = f"Sorry, you sang {run[1]} hz which is not an octave to {orig} hz."
                    
def level4setup(foreground, camera):
    temp_dict = {}
    
    temp_dict["killed"] = False
    
    temp_dict["orig_y1"] = 280 * OCTAVE
    temp_dict["orig_y2"] = 750 * OCTAVE
    temp_dict["orig_y3"] = 320 * OCTAVE
    temp_dict["orig_y4"] = 770 * OCTAVE
    temp_dict["orig_y5"] = 360 * OCTAVE
    temp_dict["orig_y6"] = 800 * OCTAVE
    temp_dict["orig_y7"] = 390 * OCTAVE
    temp_dict["orig_y8"] = 830 * OCTAVE
    temp_dict["orig_y9"] = 420 * OCTAVE
    
    temp_dict["y1"] = temp_dict["orig_y1"]
    temp_dict["y2"] = temp_dict["orig_y2"]
    temp_dict["y3"] = temp_dict["orig_y3"]
    temp_dict["y4"] = temp_dict["orig_y4"]
    temp_dict["y5"] = temp_dict["orig_y5"]
    temp_dict["y6"] = temp_dict["orig_y6"]
    temp_dict["y7"] = temp_dict["orig_y7"]
    temp_dict["y8"] = temp_dict["orig_y8"]
    temp_dict["y9"] = temp_dict["orig_y9"]
    
    temp_dict["congrats"] = False
    
    for i in range(num_of_elements):
    
        temp_dict[f"y{i+1}_height"] = 0
        temp_dict[f"y{i+1}_height_goal"] = 0
    
    temp_dict["foreground"] = foreground
    temp_dict["camera"] = camera
    temp_dict["game_map"] = game_map
    temp_dict["running"] = True
    
    return temp_dict

def level4dialogue(variables, player):
    if ((pygame.time.get_ticks() - variables["starttime"]) > 1200) and (variables["dialogue_count"]==0):
        variables["dialogue_on"] = True
        return "sing an octave above or below each note!"
    
    if ((player.rect.x > 93*TILE_SIZE) and (variables["dialogue_count"]==4)):
        variables["dialogue_on"] = True
        variables["running"] = False
        return "congrats! you finished the level!"
    
    if (variables["wrong"] != False ):
        variables["dialogue_on"] = True
        return variables["wrong"]

Level_4 = Level(foreground, game_map, level4inputs, level4setup, level4dialogue, "1", "")