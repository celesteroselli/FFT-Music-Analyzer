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
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0'],
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
        (pygame.Rect(((3000, 300), (100, 300)))), (pygame.Rect(((3300, 300), (100, 300)))), (pygame.Rect(((3600, 300), (100, 300))))
    ]

falling = False
rock = pygame.image.load("rock.png")
rock = pygame.transform.scale(rock, (100, 100))
count = 1
rock_x = 3000
rock_y = 0

while running:
    
    handle_move(m_player)
    # Draw a solid blue circle in the center
    
    full_clap_width = 300+300+300
    
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
            hits = hit_rhythms(600)
            print(hits)
            falling = True
            
    if falling:
        
        battleship = collision_test(Rect(rock_x, rock_y, 100, 100), foreground)
        if battleship:
            foreground.remove(battleship[0])
            # for i in range(len(foreground)-1):
            #     print(foreground[i])
            #     print(battleship[0])
            #     print(foreground[i] == battleship[0])
            #     if foreground[i] == battleship[0]:
            #         foreground.pop(i)
        
        display.blit(rock, (rock_x-camera.offset.x, rock_y))
        rock_y = rock_y + 4
        if count > 3:
            falling = False
            # count = 0, rockx = 3000
            # count = 1, rockx = 3300
            # count = 2, rockx = 3600
        if rock_y > WINDOW_SIZE[1]:
            if count < (len(hits)):
                rock_y = 0
                rock_x = 3000 + hits[count]
            count = count + 1
            
    screen.blit(display, (0,0))

# Done! Time to quit.
pygame.quit()