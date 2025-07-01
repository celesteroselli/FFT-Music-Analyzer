import pygame
from physics import *
from level1 import Level_1
from level2 import Level_2
from level3 import Level_3
from level4 import Level_4
from level5 import Level_5

levels = {
    1: (Level_1, (1,1)),
    2: (Level_2, (1,2)),
    3: (Level_3, (1,3)),
    4: (Level_4, (1,4)),
    5: (Level_5, (2,1)),
}

num_levels = len(levels)

def pick(events):
    foreground = [
        (pygame.Rect((((30), (30)), (300, 50)))),
        (pygame.Rect((((30), (90)), (300, 50)))),
        (pygame.Rect((((30), (150)), (300, 50)))),
        (pygame.Rect((((30), (210)), (300, 50)))),
        (pygame.Rect((((30), (270)), (300, 50)))),
    ]
    
    display.fill((255, 255, 255))
    for i in range(num_levels):
        rect = foreground[i]
        pygame.draw.rect(display, (0, 0, 255), (rect.x, rect.y, rect.width, rect.height))
    
    for event in events:
         if event.type == pygame.MOUSEBUTTONUP:
             if event.button == 1:
                # Get the mouse position at the time of the click
                mouse_pos = event.pos
                for i in range(num_levels):
                    if foreground[i].collidepoint(mouse_pos):
                        print("clicked")
                        return False, levels[(i+1)][0], levels[(i+1)][1]
                    
    pygame.display.update()       
    return True, display
    