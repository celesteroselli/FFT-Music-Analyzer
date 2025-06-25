import pygame
from physics import WINDOW_SIZE
    

def dialogue_actions(variables):
    if (pygame.time.get_ticks() > 3000) and (variables["dialogue_count"]==0):
        variables["dialogue_on"] = True
        return "oh hey"
