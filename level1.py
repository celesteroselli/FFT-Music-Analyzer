# Simple pygame program

# Import and initialize the pygame library
import pygame
from player import *
from music import *
from pygame import *
from physics import *

pygame.init()

# Run until the user asks to quit
running = True

m_player = PlayerClass(10, 10, 30, 30)
pygame.display.flip()

y = utilities.pitch_to_frequency(5)
while running:
    draw_background()
    
    m_player.loop()
    handle_move(m_player)
    m_player.draw(display)
        
    # Draw a solid blue circle in the center
    pygame.draw.rect(display, (0, 0, 255), ((DISPLAY_SIZE[0]-200, (DISPLAY_SIZE[1])-(y/5)), (20, 10)))

    # Flip the display
    pygame.display.update()
    
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.MOUSEBUTTONUP:
            y = utilities.pitch_to_frequency(5)
            pygame.draw.rect(display, (0, 0, 255), ((DISPLAY_SIZE[0]-200, DISPLAY_SIZE[1]-(y/10)), (20, 10)))
            pygame.display.flip()
            y = harmonize(5, (5/4))
            print(y)
            
    screen.blit(pygame.transform.scale(display, WINDOW_SIZE), (0,0))

# Done! Time to quit.
pygame.quit()