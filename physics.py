import pygame
from music import *
import tileset

screen = pygame.display.set_mode([1500, 900])
WINDOW_SIZE = screen.get_size()
TILE_SIZE = 150

PLAYER_SCREEN_OFFSET = 300

GROUND_ROWS = 3

display = pygame.Surface(WINDOW_SIZE)
DISPLAY_TILES = []

bg_images = tileset.images(TILE_SIZE)
print("bg_images = " + str(bg_images))

background = []
my_img = pygame.image.load("unit3.png")
background.append(pygame.transform.scale(my_img, (my_img.get_width(), 900)))
#background.append(pygame.transform.scale(pygame.image.load("bridge.png"), (2000, 900)))

def draw_background(camera, player, foreground, mapname):
    #clear tiles, fill in background with white to clear it
    DISPLAY_TILES.clear()
    display.fill((255, 255, 255))
    parallax(camera.offset.x)
    
    import pandas as pd
    import numpy as np
    
    coolarray = tileset.go(mapname)
    
    y=0
    for row in coolarray:
        x = 0
        for tile in row:
            tile = tile.item()
            if tile >= 0:
                DISPLAY_TILES.append(pygame.Rect(x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE))
                this_image = bg_images.get(str(tile))
                display.blit(this_image, ((x*TILE_SIZE)-camera.offset.x, (y*TILE_SIZE)-camera.offset.y))
            x += 1
        y += 1
        
    #draw rectangle
    for rect in foreground:     
        pygame.draw.rect(display, (0, 0, 255), (rect.x-camera.offset.x, rect.y-camera.offset.y, rect.width, rect.height))
        DISPLAY_TILES.append(rect)
        
    #move and draw player - MUST DO LAST TO GET ALL COLLISIONS
    if (player.is_colliding() == False):
        #do gravity
        player.y_vel = player.y_vel + 0.11
    if ((camera.offset.x < 0.1) and (player.x_vel < 0)):
        player.x_vel = 0
    player.move(player.x_vel, player.y_vel, DISPLAY_TILES)
        
def collision_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list

def parallax(scroll):
    for x in range(50):
        speed = 0.3
        #first bg1 then bg2 (foreground)
        for img in background:
            display.blit(img, ((x*img.get_width()) - scroll*speed, 0))
            speed += 0.3