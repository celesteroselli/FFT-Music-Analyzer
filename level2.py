import pygame
from Fourier.player import *
from Fourier.music import *
from pygame import *
from Fourier.physics import *
from Fourier.camera import *
from Fourier.Level import Level

import numpy as np

foreground = []

game_map = "1_2"

num_of_elements = 9

factor = 6

def level2inputs(variables, events, player):
    
    camera = variables.get("camera")
    foreground = variables.get("foreground")
    
    if variables["killed"]==True:
        for i in range(num_of_elements):
            variables[f"y{i+1}_height"] = 0
            variables[f"y{i+1}_height_goal"] = 0
            variables[f"y{i+1}"] = variables[f"orig_y{i+1}"]
            variables["killed"]=False
    
    foreground = [
        #x-left = x tiles from left
        #y-top = y-1 tiles from top
        (pygame.Rect((((TILE_SIZE*10), (TILE_SIZE*16)+(100)-(variables["y1_height"]*factor)), (300, 100)))),
        (pygame.Rect((((TILE_SIZE*19), (TILE_SIZE*11)+(100)-(variables["y2_height"]*factor)), (300, 100)))),
        (pygame.Rect((((TILE_SIZE*28), (TILE_SIZE*14)+(100)-(variables["y3_height"]*factor)), (300, 100)))),
        (pygame.Rect((((TILE_SIZE*37), (TILE_SIZE*10)+(100)-(variables["y4_height"]*factor)), (300, 100)))),
        (pygame.Rect((((TILE_SIZE*46), (TILE_SIZE*15)+(100)-(variables["y5_height"]*factor)), (300, 100)))),
        (pygame.Rect((((TILE_SIZE*55), (TILE_SIZE*11)+(100)-(variables["y6_height"]*factor)), (300, 100)))),
        (pygame.Rect((((TILE_SIZE*63), (TILE_SIZE*14)+(100)-(variables["y7_height"]*factor)), (300, 100)))),
        (pygame.Rect((((TILE_SIZE*73), (TILE_SIZE*9)+(100)-(variables["y8_height"]*factor)), (300, 100)))),
        (pygame.Rect((((TILE_SIZE*82), (TILE_SIZE*14)+(100)-(variables["y9_height"]*factor)), (300, 100)))),
        (pygame.Rect((((0), (TILE_SIZE*20)), (TILE_SIZE*100, 50)))),
    ]
    
    if variables["dialogue_on"]==False:
        for i in range(num_of_elements):
            if np.absolute(variables[f"y{i+1}_height_goal"]-variables[f"y{i+1}_height"]) > 10:
                if (variables["first_move"] == True):
                    print("first move was true")
                    time.sleep(1)
                    variables["first_move"] = False
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
                        run = constraint(variables[f"y{i+1}"], variables[f"y{i+1}_max"])
                        variables["figure"] = run[2]
                        if (run[0]==True):
                            print("within constraints!")
                            variables[f"y{i+1}"] = run[1]
                            variables["last_note"] = run[1]
                            variables[f"y{i+1}_height_goal"] = variables[f"y{i+1}"] - variables[f"orig_y{i+1}"]
                            if (foreground[i].y == (player.rect.y+player.rect.h)) and (player.rect.x >= foreground[i].x) and (player.rect.x < (foreground[i].x + foreground[i].w)):
                                print("player is touching rectangle")
                            else:
                                print("player not colliding")
                        else:
                            print("not within constraints!")
                            variables["wrong"] = f"Sorry, you sang {run[1]} hz which was not within the constraints."
                    
def level2setup(foreground, camera):
    temp_dict = {}
    
    temp_dict["killed"] = False
    
    temp_dict["orig_y1"] = 440 * get_octave()
    temp_dict["orig_y2"] = 500 * get_octave()
    temp_dict["orig_y3"] = 500 * get_octave()
    temp_dict["orig_y4"] = 440 * get_octave()
    temp_dict["orig_y5"] = 500 * get_octave()
    temp_dict["orig_y6"] = 440 * get_octave()
    temp_dict["orig_y7"] = 500 * get_octave()
    temp_dict["orig_y8"] = 600 * get_octave()
    temp_dict["orig_y9"] = 500 * get_octave()
    
    #higher
    temp_dict["y1_max"] = temp_dict["orig_y1"] + 160
    
    #lower
    temp_dict["y2_max"] = temp_dict["orig_y2"] - 100
    
    #higher
    temp_dict["y3_max"] = temp_dict["orig_y3"] + 100
    
    #lower
    temp_dict["y4_max"] = temp_dict["orig_y4"] - 100
    
    #higher
    temp_dict["y5_max"] = temp_dict["orig_y5"] + 100
    
    #lower
    temp_dict["y6_max"] = temp_dict["orig_y6"] - 100
    
    #higher
    temp_dict["y7_max"] = temp_dict["orig_y7"] + 100
    
    #lower
    temp_dict["y8_max"] = temp_dict["orig_y8"] - 100
    
    #higher
    temp_dict["y9_max"] = temp_dict["orig_y9"] + 100
    
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
    temp_dict["last_note"] = 400
    
    return temp_dict

def level2dialogue(variables, player):
    if ((pygame.time.get_ticks() - variables["starttime"]) > 1200) and (variables["dialogue_count"]==0):
        variables["dialogue_on"] = True
        return "sing within the two tones you hear"
    
    if (variables["wrong"] != False ):
        variables["dialogue_on"] = True
        return variables["wrong"]
    
    if ((player.rect.x > 93*TILE_SIZE) and (variables["dialogue_count"]==4)):
        variables["dialogue_on"] = True
        variables["running"] = False
        return "congrats! you finished the level!"
    
    if (variables["figure"]):
        variables["dialogue_on"] = True
        return f"you sang {variables["last_note"]} hz"

Level_2 = Level(foreground, game_map, level2inputs, level2setup, level2dialogue, "1", "")