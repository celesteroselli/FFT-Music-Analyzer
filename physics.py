import pygame
from music import *

screen = pygame.display.set_mode([1500, 900])
WINDOW_SIZE = screen.get_size()
TILE_SIZE = 150

image = pygame.image.load("image.png")
image = pygame.transform.scale(image, (TILE_SIZE, TILE_SIZE))
GROUND_ROWS = 3

display = pygame.Surface(WINDOW_SIZE)
DISPLAY_TILES = []
def draw_background(camera, player, foreground, gamemap):
    #clear tiles, fill in background with white to clear it
    DISPLAY_TILES.clear()
    display.fill((255, 255, 255))
    
    y=0
    for row in gamemap:
        x=0
        for tile in row:
            if tile == "1":
                DISPLAY_TILES.append(pygame.Rect(x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE))
                display.blit(image, ((x*TILE_SIZE)-camera.offset.x, (y*TILE_SIZE)-camera.offset.y))
            x += 1
        y += 1
        
    #draw rectangle
    for rect in foreground:     
        pygame.draw.rect(display, (0, 0, 255), (rect.x-camera.offset.x, rect.y-camera.offset.y, rect.width, rect.height))
        DISPLAY_TILES.append(rect)
        
    #move and draw player - MUST DO LAST TO GET ALL COLLISIONS
    if (player.is_colliding() == False):
        #do gravity
        player.y_vel = player.y_vel + 0.05
    player.move(player.x_vel, player.y_vel, DISPLAY_TILES)
        
def collision_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list