import pygame
from Fourier.player import *
from Fourier.music import *
from pygame import *
from Fourier.physics import *
from Fourier.camera import *
from Fourier.Level import Level

import numpy as np

foreground = []

game_map = "2_1"

num_of_elements = 7

factor = 6

def level5inputs(variables, events, player):
    
    background = [
        (16,(pygame.Rect((((TILE_SIZE*8), (TILE_SIZE*14)), (300, 300))))),
        (18, (pygame.Rect((((TILE_SIZE*17), (TILE_SIZE*12)), (300, 300))))),
        (19, (pygame.Rect((((TILE_SIZE*26), (TILE_SIZE*7)), (300, 300))))),
        (18, (pygame.Rect((((TILE_SIZE*47), (TILE_SIZE*11)), (300, 300))))),
        (16, (pygame.Rect((((TILE_SIZE*64), (TILE_SIZE*5)), (300, 300))))),
        (17, (pygame.Rect((((TILE_SIZE*73), (TILE_SIZE*1)), (300, 300))))),
        (19, (pygame.Rect((((TILE_SIZE*82), (TILE_SIZE*5)), (300, 300))))),
    ]
    
    variables["background"] = background
    
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
        (pygame.Rect((((TILE_SIZE*8), (TILE_SIZE*16)+(100)-(variables["y1_height"]*factor)), (300, 100)))),
        (pygame.Rect((((TILE_SIZE*17), (TILE_SIZE*14)+(100)-(variables["y2_height"]*factor)), (300, 100)))),
        (pygame.Rect((((TILE_SIZE*26), (TILE_SIZE*9)+(100)-(variables["y3_height"]*factor)), (300, 100)))),
        (pygame.Rect((((TILE_SIZE*47), (TILE_SIZE*13)+(100)-(variables["y4_height"]*factor)), (300, 100)))),
        (pygame.Rect((((TILE_SIZE*64), (TILE_SIZE*7)+(100)-(variables["y5_height"]*factor)), (300, 100)))),
        (pygame.Rect((((TILE_SIZE*73), (TILE_SIZE*3)+(100)-(variables["y6_height"]*factor)), (300, 100)))),
        (pygame.Rect((((TILE_SIZE*82), (TILE_SIZE*7)+(100)-(variables["y7_height"]*factor)), (300, 100)))),
        (pygame.Rect((((0), (TILE_SIZE*20)), (TILE_SIZE*100, 50)))),
    ]
                
    #things that kill the player
    for i in [num_of_elements]:
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
                        run = harmonize(variables[f"y{i+1}"], variables[f"y{i+1}_interval"])
                        orig = run[1]
                        variables["figure"] = run[2]
                        variables["last_note"] = run[1]
                        variables["first_move"] = True
                        if run[0] == True:
                            variables[f"y{i+1}"] = run[1]
                            variables[f"y{i+1}_height_goal"] = variables[f"y{i+1}"] - variables[f"orig_y{i+1}"]
                            if (foreground[i].y == (player.rect.y+player.rect.h)) and (player.rect.x >= foreground[i].x) and (player.rect.x < (foreground[i].x + foreground[i].w)):
                                print("player is touching rectangle")
                            else:
                                print("player not colliding")
                        else:
                            variables["wrong"] = run[3]
                       
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
                    
def level5setup(foreground, camera):
    temp_dict = {}
    
    temp_dict["killed"] = False
    
    temp_dict["orig_y1"] = 440 * get_octave()
    temp_dict["orig_y2"] = 500 * get_octave()
    temp_dict["orig_y3"] = 600 * get_octave()
    temp_dict["orig_y4"] = 440 * get_octave()
    temp_dict["orig_y5"] = 500 * get_octave()
    temp_dict["orig_y6"] = 650 * get_octave()
    temp_dict["orig_y7"] = 550 * get_octave()
    
    temp_dict["y1"] = temp_dict["orig_y1"]
    temp_dict["y2"] = temp_dict["orig_y2"]
    temp_dict["y3"] = temp_dict["orig_y3"]
    temp_dict["y4"] = temp_dict["orig_y4"]
    temp_dict["y5"] = temp_dict["orig_y5"]
    temp_dict["y6"] = temp_dict["orig_y6"]
    temp_dict["y7"] = temp_dict["orig_y7"]
    
    #4:3 = P4
    #3:2 = P5
    temp_dict["y1_interval"] = 4/3
    temp_dict["y2_interval"] = 3/2
    temp_dict["y3_interval"] = 2/3
    temp_dict["y4_interval"] = 3/2
    temp_dict["y5_interval"] = 4/3
    temp_dict["y6_interval"] = 3/4
    temp_dict["y7_interval"] = 2/3
    
    temp_dict["congrats"] = False
    
    for i in range(num_of_elements):
    
        temp_dict[f"y{i+1}_height"] = 0
        temp_dict[f"y{i+1}_height_goal"] = 0
    
    temp_dict["foreground"] = foreground
    temp_dict["camera"] = camera
    temp_dict["game_map"] = game_map
    temp_dict["running"] = True
    
    return temp_dict

def level5dialogue(variables, player):
    if ((pygame.time.get_ticks() - variables["starttime"]) > 1200) and (variables["dialogue_count"]==0):
        variables["dialogue_on"] = True
        return "sing the intervals in the direction shown"
    
    if ((player.rect.x > 93*TILE_SIZE)):
        variables["dialogue_on"] = True
        variables["running"] = False
        return "congrats! you finished the level!"
    
    if (variables["wrong"] != False ):
        variables["dialogue_on"] = True
        return variables["wrong"]
    
    if (variables["figure"]):
        variables["dialogue_on"] = True
        return f"you sang {variables["last_note"]} hz"

Level_5 = Level(foreground, game_map, level5inputs, level5setup, level5dialogue, "2", "")