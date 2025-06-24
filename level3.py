# Simple pygame program

# Import and initialize the pygame library
import pygame
from player import *
from music import *
from pygame import *
from physics import *
from camera import *

pygame.init()

game_map = [
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
]

# Run until the user asks to quit
running = True

m_player = PlayerClass(10, 10, 100, 100)
camera = Camera(m_player)
follow = CamScroll(camera, m_player)

pygame.display.flip()

foreground = [
        (pygame.Rect(((3000, (WINDOW_SIZE[1])-(200)), (100, 50))))
    ]

while running:
    
    handle_move(m_player)
    
    draw_background(camera, m_player, foreground, game_map)
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
            if event.button == 1:
                # Get the mouse position at the time of the click
                mouse_pos = event.pos
                    # Check if the mouse position collides with the rect
                new_pos = (mouse_pos[0] + camera.offset.x, mouse_pos[1] + camera.offset.y)
                if foreground[0].collidepoint(new_pos):
                    print("chord test")
                    print(chord(0))
                    if (chord(0)):
                        foreground.append((pygame.Rect(((3000, (WINDOW_SIZE[1])-(260)), (100, 50)))))                      
            
    screen.blit(display, (0,0))

# Done! Time to quit.
pygame.quit()