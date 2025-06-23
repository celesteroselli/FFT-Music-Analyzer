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

ypitch = 5
y2pitch = 7
y3pitch = 9

y = utilities.pitch_to_frequency(ypitch)
y2 = utilities.pitch_to_frequency(y2pitch)
y3 = utilities.pitch_to_frequency(y3pitch)
while running:
    
    handle_move(m_player)
    # Draw a solid blue circle in the center
    
    foreground = [
        (pygame.Rect(((3000, (WINDOW_SIZE[1])-(y)), (100, 50)))), (pygame.Rect(((3100, (WINDOW_SIZE[1])-(y2)), (100, 50)))), (pygame.Rect(((3200, (WINDOW_SIZE[1])-(y3)), (100, 50))))
    ]
    
    draw_background(camera, m_player, foreground)
    m_player.draw(display, camera)
    follow.scroll()

    # Flip the display
    pygame.display.update()
    
    # Did the user click the window close button?
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
            
    screen.blit(display, (0,0))

# Done! Time to quit.
pygame.quit()