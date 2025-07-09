import pygame
from Fourier.player import *
from Fourier.music import *
from pygame import *
from Fourier.physics import *
from Fourier.camera import *
from Fourier.Level import Level

import numpy as np

foreground = []

game_map = "2_3"

num_of_elements = 8

factor = 8

def level7inputs(variables, events, player):
    
    background = [
        (8, (pygame.Rect((((TILE_SIZE*8), (TILE_SIZE*14)), (300, 300))))),
        (12, (pygame.Rect((((TILE_SIZE*17), (TILE_SIZE*12)), (300, 300))))),
        (9, (pygame.Rect((((TILE_SIZE*26), (TILE_SIZE*9)), (300, 300))))),
        (12, (pygame.Rect((((TILE_SIZE*35), (TILE_SIZE*12)), (300, 300))))),
        (12, (pygame.Rect((((TILE_SIZE*44), (TILE_SIZE*10)), (300, 300))))),
        (13, (pygame.Rect((((TILE_SIZE*65), (TILE_SIZE*9)), (300, 300))))),
        (8, (pygame.Rect((((TILE_SIZE*74), (TILE_SIZE*10)), (300, 300))))),
        (8, (pygame.Rect((((TILE_SIZE*83), (TILE_SIZE*8.5)), (300, 300))))),
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
        (pygame.Rect((((TILE_SIZE*26), (TILE_SIZE*11)+(100)-(variables["y3_height"]*factor)), (300, 100)))),
        (pygame.Rect((((TILE_SIZE*35), (TILE_SIZE*14)+(100)-(variables["y4_height"]*factor)), (300, 100)))),
        (pygame.Rect((((TILE_SIZE*44), (TILE_SIZE*12)+(100)-(variables["y5_height"]*factor)), (300, 100)))),
        (pygame.Rect((((TILE_SIZE*65), (TILE_SIZE*11)+(100)-(variables["y6_height"]*factor)), (300, 100)))),
        (pygame.Rect((((TILE_SIZE*74), (TILE_SIZE*12)+(100)-(variables["y7_height"]*factor)), (300, 100)))),
        (pygame.Rect((((TILE_SIZE*83), (TILE_SIZE*10.5)+(100)-(variables["y8_height"]*factor)), (300, 100)))),
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
                    
def level7setup(foreground, camera):
    temp_dict = {}
    
    temp_dict["killed"] = False
    
    temp_dict["orig_y1"] = 600 * get_octave()
    temp_dict["orig_y2"] = 550 * get_octave()
    temp_dict["orig_y3"] = 600 * get_octave()
    temp_dict["orig_y4"] = 450 * get_octave()
    temp_dict["orig_y5"] = 500 * get_octave()
    temp_dict["orig_y6"] = 650 * get_octave()
    temp_dict["orig_y7"] = 600 * get_octave()
    temp_dict["orig_y8"] = 550 * get_octave()
    
    temp_dict["y1"] = temp_dict["orig_y1"]
    temp_dict["y2"] = temp_dict["orig_y2"]
    temp_dict["y3"] = temp_dict["orig_y3"]
    temp_dict["y4"] = temp_dict["orig_y4"]
    temp_dict["y5"] = temp_dict["orig_y5"]
    temp_dict["y6"] = temp_dict["orig_y6"]
    temp_dict["y7"] = temp_dict["orig_y7"]
    temp_dict["y8"] = temp_dict["orig_y8"]
    
    #minor 2nd = 16:5
    #minor 3rd = 6:5
    
    #m2
    temp_dict["y1_interval"] = 16/15
    #m3
    temp_dict["y2_interval"] = 6/5
    #m2 down
    temp_dict["y3_interval"] = 15/16
    #m3
    temp_dict["y4_interval"] = 6/5
    #m3
    temp_dict["y5_interval"] = 6/5
    #m3 down
    temp_dict["y6_interval"] = 5/6
    #m2
    temp_dict["y7_interval"] = 16/15
    #m2
    temp_dict["y8_interval"] = 16/15
    
    temp_dict["congrats"] = False
    
    for i in range(num_of_elements):
    
        temp_dict[f"y{i+1}_height"] = 0
        temp_dict[f"y{i+1}_height_goal"] = 0
    
    temp_dict["foreground"] = foreground
    temp_dict["camera"] = camera
    temp_dict["game_map"] = game_map
    temp_dict["running"] = True
    
    return temp_dict

def level7dialogue(variables, player):
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

Level_7 = Level(foreground, game_map, level7inputs, level7setup, level7dialogue, "2", "")