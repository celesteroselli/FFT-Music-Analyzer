import pygame
from player import *
from music import *
from pygame import *
from physics import *
from camera import *
from Level import Level

import numpy as np

foreground = []

game_map = "3_1"

DIFF1 = 300
DIFF2 = 200

foreground = [
        #x-left = x tiles from left
        #y-top = y-1 tiles from top
        (0,(pygame.Rect((((TILE_SIZE*13), (TILE_SIZE*11)), (150, 300))))),
        (0,(pygame.Rect((((TILE_SIZE*13+DIFF1), (TILE_SIZE*11)), (150, 300))))),
        (0,(pygame.Rect((((TILE_SIZE*13+DIFF1*2), (TILE_SIZE*11)), (150, 300))))),
        
        (1,(pygame.Rect((((TILE_SIZE*28), (TILE_SIZE*10)), (150, 300))))),
        (1,(pygame.Rect((((TILE_SIZE*28+DIFF2), (TILE_SIZE*10)), (150, 300))))),
        (1,(pygame.Rect((((TILE_SIZE*28+DIFF2*2), (TILE_SIZE*10)), (150, 300))))),
        (1,(pygame.Rect((((TILE_SIZE*28+DIFF2*3), (TILE_SIZE*10)), (150, 300))))),
        
        (0, (pygame.Rect((((0), (TILE_SIZE*20)), (TILE_SIZE*100, 50))))),
]

def level9inputs(variables, events, player):

    variables["background"] = background
    
    camera = variables.get("camera")
    foreground = variables.get("foreground")
    
    variables["num_of_elements"] = len(foreground)
    
    if variables["killed"]==True:
        for i in range(variables["num_of_elements"]):
            variables["foreground"] = [
        #x-left = x tiles from left
        #y-top = y-1 tiles from top
        (0,(pygame.Rect((((TILE_SIZE*13), (TILE_SIZE*11)), (150, 300))))),
        (0,(pygame.Rect((((TILE_SIZE*13+DIFF1), (TILE_SIZE*11)), (150, 300))))),
        (0,(pygame.Rect((((TILE_SIZE*13+DIFF1*2), (TILE_SIZE*11)), (150, 300))))),
        (0, (pygame.Rect((((0), (TILE_SIZE*20)), (TILE_SIZE*100, 50))))),
]
            foreground = variables.get("foreground")
            variables["num_of_elements"] = len(foreground)
            variables["killed"]=False
                
    #things that kill the player
    for i in range(variables["num_of_elements"]):
        if (foreground[i][1].y == (player.rect.y+player.rect.h)) and (player.rect.x >= foreground[i][1].x) and (player.rect.x < (foreground[i][1].x + foreground[i][1].w)):
            print("KILLED")
            player.kill(camera)
            variables["killed"] = True
            
    for event in events:
        if event.type == pygame.MOUSEBUTTONUP:
            print("mouse button up in level1 copy")
        # Check if the left mouse button was pressed (button 1)
            if event.button == 1:
                # Get the mouse position at the time of the click
                mouse_pos = event.pos
                # Check if the mouse position collides with the rect
                new_pos = (mouse_pos[0] + camera.offset.x, mouse_pos[1] + camera.offset.y)
                for i in range(variables["num_of_elements"]):
                    if foreground[i][1].collidepoint(new_pos):
                        if foreground[i][0]==0:
                            variables["current_rocks"] = 0
                            variables["start"] = 13*TILE_SIZE
                            run = hit_rhythms(DIFF1*2)
                        elif foreground[i][0]==1:
                            variables["current_rocks"] = 1
                            variables["start"] = 28*TILE_SIZE
                            run = hit_rhythms(DIFF2*3)
                        variables["hits"] = run[0]
                        variables["figure"] = run[1]
                        variables["first_move"] = True
                        variables["falling"] = True
                        variables["rock_count"] = 1
                        
    if variables["falling"] and (not variables["figure"]):
        variables["falling"] = True
        battleship = collision_test(Rect(variables["rock_x"], variables["rock_y"]+ camera.offset.y, 100, 100), foreground)
        if battleship:
            variables["foreground"].remove((variables["current_rocks"],battleship[0]))
        
        display.blit(variables["rock"], (variables["rock_x"]-camera.offset.x, variables["rock_y"]))
        variables["rock_y"] = variables["rock_y"] + 4
        if variables["rock_count"] > 3:
            variables["falling"] = False
        if variables["rock_y"] > WINDOW_SIZE[1]:
            if variables["rock_count"] < len(variables["hits"]):
                variables["rock_y"] = 0
                variables["rock_x"] = variables["start"] + variables["hits"][variables["rock_count"]]
            variables["rock_count"] = variables["rock_count"] + 1
                    
def level9setup(foreground, camera):
    temp_dict = {}
    
    temp_dict["killed"] = False
    temp_dict["current_rocks"] = 0
    
    temp_dict["congrats"] = False
    temp_dict["num_of_elements"] = 3
    
    temp_dict["foreground"] = foreground
    temp_dict["camera"] = camera
    temp_dict["game_map"] = game_map
    temp_dict["running"] = True
    
    temp_dict["rock"] = pygame.transform.scale(pygame.image.load("rock.png"), (100,100))
    temp_dict["rock_count"] = 1
    temp_dict["rock_x"] = TILE_SIZE*13
    temp_dict["rock_y"] = 0
    temp_dict["falling"] = False
    temp_dict["hits"] = None
    
    temp_dict["start"] = 13*TILE_SIZE
    
    return temp_dict

def level9dialogue(variables, player):
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
        return f"here is the audio depiction of your rhythm"

Level_9 = Level(foreground, game_map, level9inputs, level9setup, level9dialogue, "3", "")