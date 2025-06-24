# Simple pygame program

# Import and initialize the pygame library
import pygame
from player import *
from music import *
from pygame import *
from physics import *
from camera import *

from level1 import Level_1

pygame.font.init() # you have to call this at the start, 
my_font = pygame.font.SysFont('Comic Sans MS', 30)

foreground, game_map = Level_1.setup_func()

pygame.init()

# Run until the user asks to quit
running = True
m_player = PlayerClass(PLAYER_SCREEN_OFFSET, 10, 100, 100)
camera = Camera(m_player)
follow = CamScroll(camera, m_player)

dialogue_on = False
new_dialogue = False

dialogue_box = pygame.Rect(100, WINDOW_SIZE[1]-100, WINDOW_SIZE[0]-200, 50)

def do_dialogue(write):
    pygame.draw.rect(display, (0, 255, 0), dialogue_box)
    text_surface = my_font.render(write, False, (0,0,255), None)
    display.blit(text_surface, (dialogue_box.x,dialogue_box.y))

clock = pygame.time.Clock()
while running:
    
    if (not dialogue_on):
        #freezes screen if dialogue!
        handle_move(m_player)
        draw_background(camera, m_player, foreground, game_map)
        m_player.draw(display, camera)
        follow.scroll()
    else:
        if (new_dialogue):
            do_dialogue("hey!")
            new_dialogue = False
    
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        Level_1.input_func()                
            
    screen.blit(display, (0,0))
    pygame.display.update()
    clock.tick(120)

# Done! Time to quit.
pygame.quit()