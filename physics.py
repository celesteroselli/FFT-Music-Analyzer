import pygame
from music import *
import tileset

screen = pygame.display.set_mode([1500, 900])
WINDOW_SIZE = screen.get_size()
TILE_SIZE = 150

PLAYER_SCREEN_OFFSET = 300

ground_lt = pygame.image.load("ground_left_top.png")
ground_rt = pygame.image.load("ground_right_top.png")
ground_lb = pygame.image.load("ground_left_bot.png")
ground_rb = pygame.image.load("ground_right_bot.png")

ground_lt = pygame.transform.scale(ground_lt, (TILE_SIZE, TILE_SIZE))
ground_rt = pygame.transform.scale(ground_rt, (TILE_SIZE, TILE_SIZE))
ground_lb = pygame.transform.scale(ground_lb, (TILE_SIZE, TILE_SIZE))
ground_rb = pygame.transform.scale(ground_rb, (TILE_SIZE, TILE_SIZE))
GROUND_ROWS = 3

display = pygame.Surface(WINDOW_SIZE)
DISPLAY_TILES = []

bg_images = tileset.images()

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
            DISPLAY_TILES.append(pygame.Rect(x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE))
            display.blit(bg_images.get(str(tile)), ((x*TILE_SIZE)-camera.offset.x, (y*TILE_SIZE)-camera.offset.y))
            x += 1
        y += 1
        
    #draw rectangle
    for rect in foreground:     
        pygame.draw.rect(display, (0, 0, 255), (rect.x-camera.offset.x, rect.y-camera.offset.y, rect.width, rect.height))
        DISPLAY_TILES.append(rect)
        
    #move and draw player - MUST DO LAST TO GET ALL COLLISIONS
    if (player.is_colliding() == False):
        #do gravity
        player.y_vel = player.y_vel + 0.07
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
        for img in bg_images:
            display.blit(img, ((x*bg_width) - scroll*speed, 0))
            speed += 0.3