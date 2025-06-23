# Simple pygame program

# Import and initialize the pygame library
import pygame
from player import *
from music import *
from pygame import *
from physics import *
from camera import *

pygame.init()

# Run until the user asks to quit
running = True

m_player = PlayerClass(10, 10, 100, 100)
camera = Camera(m_player)
follow = CamScroll(camera, m_player)

pygame.display.flip()

y = utilities.pitch_to_frequency(5)
while running:
    
    handle_move(m_player)
    # Draw a solid blue circle in the center
    rectangle = pygame.Rect(((3000, (WINDOW_SIZE[1])-(y)), (100, 50)))
    
    draw_background(camera, m_player, rectangle)
    m_player.draw(display, camera)
    follow.scroll()

    # Flip the display
    pygame.display.update()
    
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.MOUSEBUTTONUP:
            y = utilities.pitch_to_frequency(5)
            pygame.draw.rect(display, (0, 0, 255), ((WINDOW_SIZE[0]-200, WINDOW_SIZE[1]-(y/10)), (20, 10)))
            pygame.display.flip()
            y = harmonize(5, (5/4))
            print(y)
            
    screen.blit(display, (0,0))

# Done! Time to quit.
pygame.quit()