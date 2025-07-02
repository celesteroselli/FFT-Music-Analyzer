import pygame
from physics import *
from level1 import Level_1
from level2 import Level_2
from level3 import Level_3
from level4 import Level_4
from level5 import Level_5
from level6 import Level_6
from level7 import Level_7
from level8 import Level_8

levels = {
    1: (Level_1, (1,1)),
    2: (Level_2, (1,2)),
    3: (Level_3, (1,3)),
    4: (Level_4, (1,4)),
    5: (Level_5, (2,1)),
    6: (Level_6, (2,2)),
    7: (Level_7, (2,3)),
    8: (Level_8, (2,3)),
}

MARGIN = 40
WINDOWX = WINDOW_SIZE[0] - MARGIN*2
WINDOWY = WINDOW_SIZE[1]

GAP = WINDOWX / 4
TOP = WINDOWY - MARGIN*2 - (GAP+MARGIN*4)

LEVEL_H = 100
LEVEL_W = 230

num_levels = len(levels)

def pick(events):
    background = pygame.image.load("loading.png")
    background = pygame.transform.scale(background, WINDOW_SIZE)
    display.blit(background, (0,0))

    title_surface = title_font.render("welcome to timbre", False, color1, None)

    u1surface = my_font.render("Unit 1: Pitch", False, color2, None)
    u2surface = my_font.render("Unit 2: Harmony", False, color2, None)
    u3surface = my_font.render("Unit 3: Rhythm", False, color2, None)
    u4surface = my_font.render("Unit 4: Chords", False, color2, None)

    display.blit(u1surface, (MARGIN - (u1surface.get_width()-LEVEL_W)/2,TOP-50))
    display.blit(u2surface, (MARGIN+GAP - (u2surface.get_width()-LEVEL_W)/2,TOP-50))
    display.blit(u3surface, (MARGIN+GAP*2 - (u3surface.get_width()-LEVEL_W)/2,TOP-50))
    display.blit(u4surface, (MARGIN+GAP*3 - (u4surface.get_width()-LEVEL_W)/2,TOP-50))

    display.blit(title_surface, ((WINDOW_SIZE[0]-title_surface.get_width())/2,100))

    foreground = [
        (pygame.Rect((((MARGIN), (TOP+MARGIN)), (LEVEL_W, LEVEL_H)))),
        (pygame.Rect((((MARGIN), (TOP+MARGIN*2+LEVEL_H)), (LEVEL_W, LEVEL_H)))),
        (pygame.Rect((((MARGIN), (TOP+MARGIN*3+LEVEL_H*2)), (LEVEL_W, LEVEL_H)))),
        (pygame.Rect((((MARGIN), (TOP+MARGIN*4+LEVEL_H*3)), (LEVEL_W, LEVEL_H)))),

        (pygame.Rect((((MARGIN+GAP), (TOP+MARGIN)), (LEVEL_W, LEVEL_H)))),
        (pygame.Rect((((MARGIN+GAP), (TOP+MARGIN*2+LEVEL_H)), (LEVEL_W, LEVEL_H)))),
        (pygame.Rect((((MARGIN+GAP), (TOP+MARGIN*3+LEVEL_H*2)), (LEVEL_W, LEVEL_H)))),
        (pygame.Rect((((MARGIN+GAP), (TOP+MARGIN*4+LEVEL_H*3)), (LEVEL_W, LEVEL_H)))),
    ]
    
    for i in range(num_levels):
        num = i+1
        if num > 4:
            num = num - 4
        rect = foreground[i]
        pygame.draw.rect(display, color3, (rect.x, rect.y, rect.width, rect.height))
        levelnum = my_font.render(f"Level {num}", False, color2, None)
        display.blit(levelnum, ((rect.x)+(rect.w-levelnum.get_width())/2, (rect.y)+(rect.h-levelnum.get_height())/2))
    
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
    