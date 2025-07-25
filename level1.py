import pygame
from Fourier.player import *
from Fourier.music import *
from pygame import *
from Fourier.physics import *
from Fourier.camera import *
from Fourier.Level import Level

import numpy as np

foreground = []

game_map = "1_1"

num_of_elements = 9

factor = 6

def level1inputs(variables, events, player):
    
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
        (pygame.Rect((((TILE_SIZE*9), (TILE_SIZE*16)+(100)-(variables["y1_height"]*factor)), (300, 100)))),
        (pygame.Rect((((TILE_SIZE*16), (TILE_SIZE*14)+(100)-(variables["y2_height"]*factor)), (300, 100)))),
        (pygame.Rect((((TILE_SIZE*23), (TILE_SIZE*9)+(100)-(variables["y3_height"]*factor)), (300, 100)))),
        (pygame.Rect((((TILE_SIZE*41), (TILE_SIZE*15)+(100)-(variables["y4_height"]*factor)), (300, 100)))),
        (pygame.Rect((((TILE_SIZE*56), (TILE_SIZE*10)+(100)-(variables["y5_height"]*factor)), (300, 100)))),
        (pygame.Rect((((TILE_SIZE*66), (TILE_SIZE*16)+(100)-(variables["y6_height"]*factor)), (300, 100)))),
        (pygame.Rect((((TILE_SIZE*73), (TILE_SIZE*14)+(100)-(variables["y7_height"]*factor)), (300, 100)))),
        (pygame.Rect((((TILE_SIZE*80), (TILE_SIZE*8)+(100)-(variables["y8_height"]*factor)), (300, 100)))),
        (pygame.Rect((((TILE_SIZE*88), (TILE_SIZE*13)+(100)-(variables["y9_height"]*factor)), (300, 100)))),
        (-20, (pygame.Rect((((TILE_SIZE*79), (TILE_SIZE*13)), (600, 50))))),
        (pygame.Rect((((0), (TILE_SIZE*20)), (TILE_SIZE*100, 50)))),
    ]
                
    #things that kill the player
    if (foreground[10].y == (player.rect.y+player.rect.h)) and (player.rect.x >= foreground[10].x) and (player.rect.x < (foreground[10].x + foreground[10].w)):
        print("KILLED")
        player.kill(camera)
        variables["killed"] = True
        
    if (foreground[9][1].y == (player.rect.y+player.rect.h)) and (player.rect.x >= foreground[9][1].x) and (player.rect.x < (foreground[9][1].x + foreground[9][1].w)):
        print("KILLED")
        player.kill(camera)
        variables["killed"] = True
    
    variables["foreground"] = foreground
            
    for event in events:
        if event.type == pygame.MOUSEBUTTONUP:
        # Check if the left mouse button was pressed (button 1)
            if event.button == 1:
                # Get the mouse position at the time of the click
                mouse_pos = event.pos
                # Check if the mouse position collides with the rect
                new_pos = (mouse_pos[0] + camera.offset.x, mouse_pos[1] + camera.offset.y)
                for i in range(num_of_elements):
                    if foreground[i].collidepoint(new_pos):
                        run = pitch(variables[f"y{i+1}"])
                        if (run[0] < USER_CHORD_MAX) and (run[0] > USER_CHORD_MIN): 
                            variables[f"y{i+1}"] = run[0]
                            variables["figure"] = run[1]
                            variables["last_note"] = run[0]
                            variables["first_move"] = True
                            variables[f"y{i+1}_height_goal"] = variables[f"y{i+1}"] - variables[f"orig_y{i+1}"]
                            if (foreground[i].y == (player.rect.y+player.rect.h)) and (player.rect.x >= foreground[i].x) and (player.rect.x < (foreground[i].x + foreground[i].w)):
                                print("player is touching rectangle")
                            else:
                                print("player not colliding")
                        else:
                            variables["wrong"] = "Sorry, you were too high or too low to hear. Try again!"
                       
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
                    
def level1setup(foreground, camera):
    temp_dict = {}
    
    temp_dict["killed"] = False
    
    temp_dict["orig_y1"] = 440 * get_octave()
    temp_dict["orig_y2"] = 500 * get_octave()
    temp_dict["orig_y3"] = 600 * get_octave()
    temp_dict["orig_y4"] = 440 * get_octave()
    temp_dict["orig_y5"] = 600 * get_octave()
    temp_dict["orig_y6"] = 440 * get_octave()
    temp_dict["orig_y7"] = 500 * get_octave()
    temp_dict["orig_y8"] = 600 * get_octave()
    temp_dict["orig_y9"] = 500 * get_octave()
    
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

def level1dialogue(variables, player):
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
    
    if ((player.rect.x > 93*TILE_SIZE)):
        variables["dialogue_on"] = True
        variables["running"] = False
        return "congrats! you finished the level!"
    
    if (variables["figure"]):
        variables["dialogue_on"] = True
        return f"you sang {variables["last_note"]} hz"
    
    if (variables["wrong"] != False ):
        variables["dialogue_on"] = True
        return variables["wrong"]

Level_1 = Level(foreground, game_map, level1inputs, level1setup, level1dialogue, "1", "")