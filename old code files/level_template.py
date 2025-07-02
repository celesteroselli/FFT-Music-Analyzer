# Import and initialize the pygame library
import pygame
from player import *
from music import *
from pygame import *
from physics import *
from camera import *
from usersettings import *

pygame.init()

game_map = []

# Run until the user asks to quit
running = True

#establish player objects
m_player = PlayerClass(PLAYER_SCREEN_OFFSET, 10, 100, 100)
camera = Camera(m_player)
follow = CamScroll(camera, m_player)

#establish foreground
foreground = []

#establish dialog settings
dialogue_on = False
new_dialogue = False

dialogue_box = pygame.Rect(100, WINDOW_SIZE[1]-100, WINDOW_SIZE[0]-200, 50)

def do_dialogue(write):
    pygame.draw.rect(display, (0, 255, 0), dialogue_box)
    text_surface = my_font.render(write, False, color1, None)
    display.blit(text_surface, (dialogue_box.x,dialogue_box.y))

clock = pygame.time.Clock()
while running:
    #IF FOREGROUND MUST BE EDITED, PUT BELOW HERE:
    
    
    
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
            
        #PUT EXTRA INPUTS BELOW HERE:  
        
        
            
    screen.blit(display, (0,0))
    pygame.display.update()
    clock.tick(120)

# Done! Time to quit.
pygame.quit()