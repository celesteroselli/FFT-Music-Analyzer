import pygame
from player import *
from music import *
from pygame import *
from physics import *
from camera import *

def level1inputs(variables):
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
            
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        # TO GET MOUSE POSITION IN REAL-WORLD COORDINATES: new_pos = (mouse_pos[0] + camera.offset.x, mouse_pos[1] + camera.offset.y)
        # TO GET PLAYER POSITION IN REAL-WORLD COORDINATES: new_player_pos = (m_player.rect.x + camera.offset.x, m_player.rect.y + camera.offset.y)
        
        if event.type == pygame.MOUSEBUTTONUP:
        # Check if the left mouse button was pressed (button 1)
            if event.button == 1:
                # Get the mouse position at the time of the click
                mouse_pos = event.pos
                # Check if the mouse position collides with the rect
                new_pos = (mouse_pos[0] + camera.offset.x, mouse_pos[1] + camera.offset.y)
                if foreground[0].collidepoint(new_pos):
                    print("collided w 1")
                    y = harmonize(ypitch, (5/4))
                if foreground[1].collidepoint(new_pos):
                    print("collided w 2")
                    y2 = harmonize(y2pitch, (5/4))
                if foreground[2].collidepoint(new_pos):
                    print("collided w 3")
                    y3 = harmonize(y3pitch, (5/4))
                    
                    
def level1setup(foreground, camera):
    ypitch = 5
    y2pitch = 7
    y3pitch = 9

    y = utilities.pitch_to_frequency(ypitch)
    y2 = utilities.pitch_to_frequency(y2pitch)
    y3 = utilities.pitch_to_frequency(y3pitch)
    
    return (["ypitch", ypitch], ["y2pitch", y2pitch], ["y3pitch", y3pitch,] ["y", y], ["y2", y2], ["y3", y3], ["foreground", foreground], ["camera", camera])