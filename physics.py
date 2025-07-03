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

unit1bg = pygame.image.load("unit1.jpeg")
unit1fg = pygame.image.load("u1foreground.png")
unit2bg = pygame.image.load("unit2.png")
unit3bg = pygame.image.load("unit3.jpeg")
unit4bg = pygame.image.load("unit4.png")

images = {
    "1": pygame.transform.scale(unit1bg, (unit1bg.get_width(), 900)),
    "1fg": pygame.transform.scale(unit1fg, (unit1fg.get_width()/2, 450)),
    "2": pygame.transform.scale(unit2bg, (unit1bg.get_width(), 900)),
    "3": pygame.transform.scale(unit3bg, (unit1bg.get_width(), 900)),
    "4": pygame.transform.scale(unit4bg, (unit1bg.get_width(), 900)),
}

background = []
# background.append(pygame.transform.scale(my_img, (my_img.get_width(), 900)))
# background.append(pygame.transform.scale(my_foreground, (my_img.get_width()/2, 450)))
#background.append(pygame.transform.scale(pygame.image.load("bridge.png"), (2000, 900)))

platform = pygame.image.load("platform.png").convert_alpha()
platform = pygame.transform.scale(platform, (300, 60))

def draw_background(camera, player, foreground, mapname, draw_back, game_back, game_front):
    #clear tiles, fill in background with white to clear it
    DISPLAY_TILES.clear()
    display.fill((255, 255, 255))
    parallax(camera.offset.x, game_back, game_front)
    
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
        display.blit(platform, (rect.x-camera.offset.x, rect.y-camera.offset.y))
        #pygame.draw.rect(display, (0, 0, 255), (rect.x-camera.offset.x, rect.y-camera.offset.y, rect.width, rect.height))
        DISPLAY_TILES.append(rect)
        
    for rect in draw_back:     
        pygame.draw.rect(display, (0, 0, 255), (rect.x-camera.offset.x, rect.y-camera.offset.y, rect.width, rect.height))
        
    #move and draw player - MUST DO LAST TO GET ALL COLLISIONS
    if (player.is_colliding() == False):
        #do gravity
        player.y_vel = player.y_vel + 0.11
        player.animate = "jump"
        player.ticker = 0.3
    if ((camera.offset.x < 0.12) and (player.x_vel < 0)):
        player.x_vel = 0
        player.animate = "idle"
        player.ticker = 0.7
    player.move(player.x_vel, player.y_vel, DISPLAY_TILES)
        
def collision_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list

def parallax(scroll, game_back, game_front):
    if game_front:
        background = [images[game_back], images[game_front]]
    else:
        background = [images[game_back]]
    for x in range(50):
        speed = 0.3
        #first bg1 then bg2 (foreground)
        for img in background:
            display.blit(img, ((x*img.get_width()) - scroll*speed, WINDOW_SIZE[1]-img.get_height()))
            speed += 0.3