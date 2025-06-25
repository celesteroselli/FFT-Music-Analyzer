import pygame
from player import *
from music import *
from pygame import *
from physics import *
from camera import *
from Level import Level

foreground = []

game_map = "1_1"

# foreground = [
#         (pygame.Rect(((3000, (WINDOW_SIZE[1])-(y)), (100, 50)))), (pygame.Rect(((3100, (WINDOW_SIZE[1])-(y2)), (100, 50)))), (pygame.Rect(((3200, (WINDOW_SIZE[1])-(y3)), (100, 50))))
# ]

def level1inputs(variables, events):
    global y
    global y2
    global y3
    
    global ypitch
    global y2pitch
    global y3pitch
    
    global camera
    camera = variables.get("camera")
    global foreground
    foreground = variables.get("foreground")
    
    y = variables.get("y")
    y2 = variables.get("y2")
    y3 = variables.get("y3")
    
    ypitch = variables.get("ypitch")
    y2pitch = variables.get("y2pitch")
    y3pitch = variables.get("y3pitch")
    
    global running
    running = variables.get("running")
    
    foreground = [
        (pygame.Rect(((3000, (WINDOW_SIZE[1])-(y)), (100, 50)))), (pygame.Rect(((3100, (WINDOW_SIZE[1])-(y2)), (100, 50)))), (pygame.Rect(((3200, (WINDOW_SIZE[1])-(y3)), (100, 50))))
    ]
    
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
                    print("collided w 1")
                    y = harmonize(ypitch, (5/4))
                    variables["y"] = y
                if foreground[1].collidepoint(new_pos):
                    print("collided w 2")
                    y2 = harmonize(y2pitch, (5/4))
                    variables["y2"] = y2
                if foreground[2].collidepoint(new_pos):
                    print("collided w 3")
                    y3 = harmonize(y3pitch, (5/4))
                    variables["y3"] = y3
                    
def level1setup(foreground, camera):
    ypitch = 5
    y2pitch = 7
    y3pitch = 9

    y = utilities.pitch_to_frequency(ypitch)
    y2 = utilities.pitch_to_frequency(y2pitch)
    y3 = utilities.pitch_to_frequency(y3pitch)
    
    return (["ypitch", ypitch], ["y2pitch", y2pitch], ["y3pitch", y3pitch], ["y", y], ["y2", y2], ["y3", y3], ["foreground", foreground], ["camera", camera], ["running", True], ["game_map", game_map])

def level1dialogue(variables):
    if ((pygame.time.get_ticks() - variables["starttime"]) > 3000) and (variables["dialogue_count"]==0):
        variables["dialogue_on"] = True
        return "oh hey"

Level_1 = Level(foreground, game_map, level1inputs, level1setup, level1dialogue)