import pygame
from player import *
from music import *
from pygame import *
from physics import *
from camera import *
from Level import Level

import numpy as np

foreground = []

game_map = "3_2"

DIFF1 = 120
DIFF2 = 120
DIFF3 = 120
DIFF4 = 120
DIFF5 = 120
DIFF6 = 120

foreground = [
        #x-left = x tiles from left
        #y-top = y-1 tiles from top
        
        (0,(pygame.Rect((((TILE_SIZE*12), (TILE_SIZE*14)-80), (128, 380))))),
        #1
        (0,(pygame.Rect((((TILE_SIZE*12+DIFF1*2), (TILE_SIZE*14)-80), (128, 380))))),
        #1
        (0,(pygame.Rect((((TILE_SIZE*12+DIFF1*4), (TILE_SIZE*14)-80), (128, 380))))),
        #0.5
        (0,(pygame.Rect((((TILE_SIZE*12+DIFF1*5), (TILE_SIZE*14)-80), (128, 380))))),
        #0.5
        (0,(pygame.Rect((((TILE_SIZE*12+DIFF1*6), (TILE_SIZE*14)-80), (128, 380))))),
        #1
        
        
        (1,(pygame.Rect((((TILE_SIZE*25), (TILE_SIZE*13)-80), (150, 300))))),
        #1
        (1,(pygame.Rect((((TILE_SIZE*25+DIFF2*2), (TILE_SIZE*13)-80), (150, 300))))),
        #0.5
        (1,(pygame.Rect((((TILE_SIZE*25+DIFF2*3), (TILE_SIZE*13)-80), (150, 300))))),
        #0.5
        (1,(pygame.Rect((((TILE_SIZE*25+DIFF2*4), (TILE_SIZE*13)-80), (150, 300))))),
        #1
        
        (2,(pygame.Rect((((TILE_SIZE*40), (TILE_SIZE*13)-80), (150, 300))))),
        #0.5
        (2,(pygame.Rect((((TILE_SIZE*40+DIFF3), (TILE_SIZE*13)-80), (150, 300))))),
        #0.5
        (2,(pygame.Rect((((TILE_SIZE*40+DIFF3*2), (TILE_SIZE*13)-80), (150, 300))))),
        #1
        (2,(pygame.Rect((((TILE_SIZE*40+DIFF3*4), (TILE_SIZE*13)-80), (150, 300))))),
        #0.5
        (2,(pygame.Rect((((TILE_SIZE*40+DIFF3*5), (TILE_SIZE*13)-80), (150, 300))))),
        #0.5
        (2,(pygame.Rect((((TILE_SIZE*40+DIFF3*6), (TILE_SIZE*13)-80), (150, 300))))),
        #1
        
        (3,(pygame.Rect((((TILE_SIZE*53), (TILE_SIZE*12)-80), (150, 300))))),
        #0.5
        (3,(pygame.Rect((((TILE_SIZE*53+DIFF4), (TILE_SIZE*12)-80), (150, 300))))),
        #0.5
        (3,(pygame.Rect((((TILE_SIZE*53+DIFF4*2), (TILE_SIZE*12)-80), (150, 300))))),
        #0.5
        (3,(pygame.Rect((((TILE_SIZE*53+DIFF4*3), (TILE_SIZE*12)-80), (150, 300))))),
        #0.5
        (3,(pygame.Rect((((TILE_SIZE*53+DIFF4*4), (TILE_SIZE*12)-80), (150, 300))))),
        #1
        (3,(pygame.Rect((((TILE_SIZE*53+DIFF4*6), (TILE_SIZE*12)-80), (150, 300))))),
        #1
        
        
        (4,(pygame.Rect((((TILE_SIZE*66), (TILE_SIZE*11)-80), (150, 300))))),
        #1
        (4,(pygame.Rect((((TILE_SIZE*66+DIFF5*2), (TILE_SIZE*11)-80), (150, 300))))),
        #1
        (4,(pygame.Rect((((TILE_SIZE*66+DIFF5*4), (TILE_SIZE*11)-80), (150, 300))))),
        #1
        (4,(pygame.Rect((((TILE_SIZE*66+DIFF5*6), (TILE_SIZE*11)-80), (150, 300))))),
        #0.5
        (4,(pygame.Rect((((TILE_SIZE*66+DIFF5*7), (TILE_SIZE*11)-80), (150, 300))))),
        #0.5
        
        (5,(pygame.Rect((((TILE_SIZE*80), (TILE_SIZE*11)-80), (150, 300))))),
        #1
        (5,(pygame.Rect((((TILE_SIZE*80+DIFF6*2), (TILE_SIZE*11)-80), (150, 300))))),
        #0.5
        (5,(pygame.Rect((((TILE_SIZE*80+DIFF6*3), (TILE_SIZE*11)-80), (150, 300))))),
        #0.5
        (5,(pygame.Rect((((TILE_SIZE*80+DIFF6*4), (TILE_SIZE*11)-80), (150, 300))))),
        #1
        (5,(pygame.Rect((((TILE_SIZE*80+DIFF6*6), (TILE_SIZE*11)-80), (150, 300))))),
        #0.5
        (5,(pygame.Rect((((TILE_SIZE*80+DIFF6*7), (TILE_SIZE*11)-80), (150, 300))))),
        #0.5
        
        (0, (pygame.Rect((((0), (TILE_SIZE*20)), (TILE_SIZE*100, 50))))),
]

def level10inputs(variables, events, player):
    variables["background"] = background
    
    camera = variables.get("camera")
    foreground = variables.get("foreground")
    
    variables["num_of_elements"] = len(foreground)
    
    if variables["killed"]==True:
        for i in range(variables["num_of_elements"]):
            variables["foreground"] = [
        #x-left = x tiles from left
        #y-top = y-1 tiles from top
        
        (0,(pygame.Rect((((TILE_SIZE*12), (TILE_SIZE*14)-80), (128, 380))))),
        #1
        (0,(pygame.Rect((((TILE_SIZE*12+DIFF1*2), (TILE_SIZE*14)-80), (128, 380))))),
        #1
        (0,(pygame.Rect((((TILE_SIZE*12+DIFF1*4), (TILE_SIZE*14)-80), (128, 380))))),
        #0.5
        (0,(pygame.Rect((((TILE_SIZE*12+DIFF1*5), (TILE_SIZE*14)-80), (128, 380))))),
        #0.5
        (0,(pygame.Rect((((TILE_SIZE*12+DIFF1*6), (TILE_SIZE*14)-80), (128, 380))))),
        #1
        
        
        (1,(pygame.Rect((((TILE_SIZE*25), (TILE_SIZE*13)-80), (150, 300))))),
        #1
        (1,(pygame.Rect((((TILE_SIZE*25+DIFF2*2), (TILE_SIZE*13)-80), (150, 300))))),
        #0.5
        (1,(pygame.Rect((((TILE_SIZE*25+DIFF2*3), (TILE_SIZE*13)-80), (150, 300))))),
        #0.5
        (1,(pygame.Rect((((TILE_SIZE*25+DIFF2*4), (TILE_SIZE*13)-80), (150, 300))))),
        #1
        
        (2,(pygame.Rect((((TILE_SIZE*40), (TILE_SIZE*13)-80), (150, 300))))),
        #0.5
        (2,(pygame.Rect((((TILE_SIZE*40+DIFF3), (TILE_SIZE*13)-80), (150, 300))))),
        #0.5
        (2,(pygame.Rect((((TILE_SIZE*40+DIFF3*2), (TILE_SIZE*13)-80), (150, 300))))),
        #1
        (2,(pygame.Rect((((TILE_SIZE*40+DIFF3*4), (TILE_SIZE*13)-80), (150, 300))))),
        #0.5
        (2,(pygame.Rect((((TILE_SIZE*40+DIFF3*5), (TILE_SIZE*13)-80), (150, 300))))),
        #0.5
        (2,(pygame.Rect((((TILE_SIZE*40+DIFF3*6), (TILE_SIZE*13)-80), (150, 300))))),
        #1
        
        (3,(pygame.Rect((((TILE_SIZE*53), (TILE_SIZE*12)-80), (150, 300))))),
        #0.5
        (3,(pygame.Rect((((TILE_SIZE*53+DIFF4), (TILE_SIZE*12)-80), (150, 300))))),
        #0.5
        (3,(pygame.Rect((((TILE_SIZE*53+DIFF4*2), (TILE_SIZE*12)-80), (150, 300))))),
        #0.5
        (3,(pygame.Rect((((TILE_SIZE*53+DIFF4*3), (TILE_SIZE*12)-80), (150, 300))))),
        #0.5
        (3,(pygame.Rect((((TILE_SIZE*53+DIFF4*4), (TILE_SIZE*12)-80), (150, 300))))),
        #1
        (3,(pygame.Rect((((TILE_SIZE*53+DIFF4*6), (TILE_SIZE*12)-80), (150, 300))))),
        #1
        
        
        (4,(pygame.Rect((((TILE_SIZE*66), (TILE_SIZE*11)-80), (150, 300))))),
        #1
        (4,(pygame.Rect((((TILE_SIZE*66+DIFF5*2), (TILE_SIZE*11)-80), (150, 300))))),
        #1
        (4,(pygame.Rect((((TILE_SIZE*66+DIFF5*4), (TILE_SIZE*11)-80), (150, 300))))),
        #1
        (4,(pygame.Rect((((TILE_SIZE*66+DIFF5*6), (TILE_SIZE*11)-80), (150, 300))))),
        #0.5
        (4,(pygame.Rect((((TILE_SIZE*66+DIFF5*7), (TILE_SIZE*11)-80), (150, 300))))),
        #0.5
        
        (5,(pygame.Rect((((TILE_SIZE*80), (TILE_SIZE*11)-80), (150, 300))))),
        #1
        (5,(pygame.Rect((((TILE_SIZE*80+DIFF6*2), (TILE_SIZE*11)-80), (150, 300))))),
        #0.5
        (5,(pygame.Rect((((TILE_SIZE*80+DIFF6*3), (TILE_SIZE*11)-80), (150, 300))))),
        #0.5
        (5,(pygame.Rect((((TILE_SIZE*80+DIFF6*4), (TILE_SIZE*11)-80), (150, 300))))),
        #1
        (5,(pygame.Rect((((TILE_SIZE*80+DIFF6*6), (TILE_SIZE*11)-80), (150, 300))))),
        #0.5
        (5,(pygame.Rect((((TILE_SIZE*80+DIFF6*7), (TILE_SIZE*11)-80), (150, 300))))),
        #0.5
        
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
                            variables["start"] = 12*TILE_SIZE
                            variables["rock_x"] = variables["start"]
                            variables["max_hits"] = 5
                            run = hit_rhythms(DIFF1*(6))
                        elif foreground[i][0]==1:
                            variables["current_rocks"] = 1
                            variables["start"] = 25*TILE_SIZE
                            variables["rock_x"] = variables["start"]
                            variables["max_hits"] = 4
                            run = hit_rhythms(DIFF2*(4))
                        elif foreground[i][0]==2:
                            variables["current_rocks"] = 2
                            variables["start"] = 40*TILE_SIZE
                            variables["rock_x"] = variables["start"]
                            variables["max_hits"] = 6
                            run = hit_rhythms(DIFF3*(6))
                        elif foreground[i][0]==3:
                            variables["current_rocks"] = 3
                            variables["start"] = 53*TILE_SIZE
                            variables["rock_x"] = variables["start"]
                            variables["max_hits"] = 6
                            run = hit_rhythms(DIFF4*(6))
                        elif foreground[i][0]==4:
                            variables["current_rocks"] = 4
                            variables["start"] = 66*TILE_SIZE
                            variables["rock_x"] = variables["start"]
                            variables["max_hits"] = 5
                            run = hit_rhythms(DIFF5*(7))
                        elif foreground[i][0]==5:
                            variables["current_rocks"] = 5
                            variables["start"] = 80*TILE_SIZE
                            variables["rock_x"] = variables["start"]
                            variables["max_hits"] = 6
                            run = hit_rhythms(DIFF6*(7))
                        variables["hits"] = run[0]
                        variables["figure"] = run[1]
                        variables["first_move"] = True
                        variables["falling"] = True
                        
    if variables["falling"] and (not variables["figure"]):
        if (variables["rock_count"] > len(variables["hits"])) or (variables["rock_count"] > variables["max_hits"]):
            print("sunk", variables["sunk"], "max-hits", variables["max_hits"])
            if variables["sunk"]==variables["max_hits"]:
                print("you did fine bro")
                variables["sunk"] = 0
                variables["falling"] = False
                variables["rock_count"] = 0
            else:
                print("you failed bro")
                variables["sunk"] = 0
                variables["falling"] = False
                variables["rock_count"] = 0
                variables["foreground"] = [
        (0,(pygame.Rect((((TILE_SIZE*12), (TILE_SIZE*14)-80), (128, 380))))),
        #1
        (0,(pygame.Rect((((TILE_SIZE*12+DIFF1*2), (TILE_SIZE*14)-80), (128, 380))))),
        #1
        (0,(pygame.Rect((((TILE_SIZE*12+DIFF1*4), (TILE_SIZE*14)-80), (128, 380))))),
        #0.5
        (0,(pygame.Rect((((TILE_SIZE*12+DIFF1*5), (TILE_SIZE*14)-80), (128, 380))))),
        #0.5
        (0,(pygame.Rect((((TILE_SIZE*12+DIFF1*6), (TILE_SIZE*14)-80), (128, 380))))),
        #1
        
        
        (1,(pygame.Rect((((TILE_SIZE*25), (TILE_SIZE*13)-80), (150, 300))))),
        #1
        (1,(pygame.Rect((((TILE_SIZE*25+DIFF2*2), (TILE_SIZE*13)-80), (150, 300))))),
        #0.5
        (1,(pygame.Rect((((TILE_SIZE*25+DIFF2*3), (TILE_SIZE*13)-80), (150, 300))))),
        #0.5
        (1,(pygame.Rect((((TILE_SIZE*25+DIFF2*4), (TILE_SIZE*13)-80), (150, 300))))),
        #1
        
        (2,(pygame.Rect((((TILE_SIZE*40), (TILE_SIZE*13)-80), (150, 300))))),
        #0.5
        (2,(pygame.Rect((((TILE_SIZE*40+DIFF3), (TILE_SIZE*13)-80), (150, 300))))),
        #0.5
        (2,(pygame.Rect((((TILE_SIZE*40+DIFF3*2), (TILE_SIZE*13)-80), (150, 300))))),
        #1
        (2,(pygame.Rect((((TILE_SIZE*40+DIFF3*4), (TILE_SIZE*13)-80), (150, 300))))),
        #0.5
        (2,(pygame.Rect((((TILE_SIZE*40+DIFF3*5), (TILE_SIZE*13)-80), (150, 300))))),
        #0.5
        (2,(pygame.Rect((((TILE_SIZE*40+DIFF3*6), (TILE_SIZE*13)-80), (150, 300))))),
        #1
        
        (3,(pygame.Rect((((TILE_SIZE*53), (TILE_SIZE*12)-80), (150, 300))))),
        #0.5
        (3,(pygame.Rect((((TILE_SIZE*53+DIFF4), (TILE_SIZE*12)-80), (150, 300))))),
        #0.5
        (3,(pygame.Rect((((TILE_SIZE*53+DIFF4*2), (TILE_SIZE*12)-80), (150, 300))))),
        #0.5
        (3,(pygame.Rect((((TILE_SIZE*53+DIFF4*3), (TILE_SIZE*12)-80), (150, 300))))),
        #0.5
        (3,(pygame.Rect((((TILE_SIZE*53+DIFF4*4), (TILE_SIZE*12)-80), (150, 300))))),
        #1
        (3,(pygame.Rect((((TILE_SIZE*53+DIFF4*6), (TILE_SIZE*12)-80), (150, 300))))),
        #1
        
        
        (4,(pygame.Rect((((TILE_SIZE*66), (TILE_SIZE*11)-80), (150, 300))))),
        #1
        (4,(pygame.Rect((((TILE_SIZE*66+DIFF5*2), (TILE_SIZE*11)-80), (150, 300))))),
        #1
        (4,(pygame.Rect((((TILE_SIZE*66+DIFF5*4), (TILE_SIZE*11)-80), (150, 300))))),
        #1
        (4,(pygame.Rect((((TILE_SIZE*66+DIFF5*6), (TILE_SIZE*11)-80), (150, 300))))),
        #0.5
        (4,(pygame.Rect((((TILE_SIZE*66+DIFF5*7), (TILE_SIZE*11)-80), (150, 300))))),
        #0.5
        
        (5,(pygame.Rect((((TILE_SIZE*80), (TILE_SIZE*11)-80), (150, 300))))),
        #1
        (5,(pygame.Rect((((TILE_SIZE*80+DIFF6*2), (TILE_SIZE*11)-80), (150, 300))))),
        #0.5
        (5,(pygame.Rect((((TILE_SIZE*80+DIFF6*3), (TILE_SIZE*11)-80), (150, 300))))),
        #0.5
        (5,(pygame.Rect((((TILE_SIZE*80+DIFF6*4), (TILE_SIZE*11)-80), (150, 300))))),
        #1
        (5,(pygame.Rect((((TILE_SIZE*80+DIFF6*6), (TILE_SIZE*11)-80), (150, 300))))),
        #0.5
        (5,(pygame.Rect((((TILE_SIZE*80+DIFF6*7), (TILE_SIZE*11)-80), (150, 300))))),
        #0.5
        
        (0, (pygame.Rect((((0), (TILE_SIZE*20)), (TILE_SIZE*100, 50))))),
]
        else:
            variables["falling"] = True
            battleship = collision_test(Rect(variables["rock_x"], variables["rock_y"]+ camera.offset.y, 100, 100), foreground)
            if battleship:
                variables["sunk"] = variables["sunk"]+1
                variables["foreground"].remove((variables["current_rocks"],battleship[0]))
        
            display.blit(variables["rock"], (variables["rock_x"]-camera.offset.x, variables["rock_y"]))
            variables["rock_y"] = variables["rock_y"] + 9
            if variables["rock_y"] > WINDOW_SIZE[1]:
                if variables["rock_count"] < len(variables["hits"]):
                    variables["rock_y"] = 0
                    variables["rock_x"] = variables["start"] + variables["hits"][variables["rock_count"]]
                variables["rock_count"] = variables["rock_count"] + 1
                    
def level10setup(foreground, camera):
    temp_dict = {}
    
    temp_dict["killed"] = False
    temp_dict["current_rocks"] = 0
    
    temp_dict["congrats"] = False
    temp_dict["num_of_elements"] = 3
    
    temp_dict["foreground"] = foreground
    temp_dict["camera"] = camera
    temp_dict["game_map"] = game_map
    temp_dict["running"] = True
    
    temp_dict["rock"] = pygame.transform.scale(pygame.image.load("finalrock.png"), (100,100))
    temp_dict["rock_count"] = 1
    temp_dict["rock_x"] = TILE_SIZE*13
    temp_dict["rock_y"] = 0
    temp_dict["falling"] = False
    temp_dict["hits"] = None
    temp_dict["max_hits"] = 3
    temp_dict["sunk"] = 0
    
    temp_dict["start"] = 13*TILE_SIZE
    
    return temp_dict

def level10dialogue(variables, player):
    if ((pygame.time.get_ticks() - variables["starttime"]) > 1200) and (variables["dialogue_count"]==0):
        variables["dialogue_on"] = True
        return "clear the rocks in your path"
    
    if (player.rect.x > 11*TILE_SIZE) and (variables["dialogue_count"]==1):
        variables["dialogue_on"] = True
        return "tap the walls and clap on beat to make rocks fall"
    
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

Level_10 = Level(foreground, game_map, level10inputs, level10setup, level10dialogue, "3", "")