import pygame
from physics import *

def pick(events):
    foreground = [
        (pygame.Rect((((30), (30)), (300, 50)))),
    ]
    
    display.fill((255, 255, 255))
    rect = foreground[0]
    pygame.draw.rect(display, (0, 0, 255), (rect.x, rect.y, rect.width, rect.height))
    
    for event in events:
         if event.type == pygame.MOUSEBUTTONUP:
             if event.button == 1:
                # Get the mouse position at the time of the click
                mouse_pos = event.pos
                if foreground[0].collidepoint(mouse_pos):
                    print("clicked")
                    return False, ""
                    
    pygame.display.update()       
    return True, display
    