import pygame
from Fourier.music import *
import Fourier.tileset as tileset
from Fourier.usersettings import resource_path

screen = pygame.display.set_mode([1500, 900])
WINDOW_SIZE = screen.get_size()
TILE_SIZE = 150

PLAYER_SCREEN_OFFSET = 300

GROUND_ROWS = 3

display = pygame.Surface(WINDOW_SIZE)
DISPLAY_TILES = []

bg_images = tileset.images(TILE_SIZE)
print("bg_images = " + str(bg_images))

unit1bg = pygame.image.load(resource_path("statics/unit1.jpeg"))
unit1fg = pygame.image.load(resource_path("statics/u1foreground.png"))
unit2bg = pygame.image.load(resource_path("statics/unit2.png"))
unit3bg = pygame.image.load(resource_path("statics/unit3.jpeg"))
unit4bg = pygame.image.load(resource_path("statics/unit4.png"))

bgpitch1 = pygame.image.load(resource_path("tileset/1bgpitch.png"))
bgpitch2 = pygame.image.load(resource_path("tileset/2bgpitch.png"))
bgpitch3 = pygame.image.load(resource_path("tileset/3bgpitch.png"))
bgpitch4 = pygame.image.load(resource_path("tileset/4bgpitch.png"))
bgpitch5 = pygame.image.load(resource_path("tileset/5bgpitch.png"))
bgpitch6 = pygame.image.load(resource_path("tileset/6bgpitch.png"))
bgpitch7 = pygame.image.load(resource_path("tileset/7bgpitch.png"))
bgpitch8 = pygame.image.load(resource_path("tileset/8bgpitch.png"))
bgpitch9 = pygame.image.load(resource_path("tileset/10bgpitch.png"))
bgpitch10 = pygame.image.load(resource_path("tileset/10bgpitch.png"))
bgpitch11 = pygame.image.load(resource_path("tileset/11bgpitch.png"))
bgpitch12 = pygame.image.load(resource_path("tileset/12bgpitch.png"))
bgpitch13 = pygame.image.load(resource_path("tileset/13bgpitch.png"))
bgpitch14 = pygame.image.load(resource_path("tileset/14bgpitch.png"))
bgpitch15 = pygame.image.load(resource_path("tileset/15bgpitch.png"))
bgpitch16 = pygame.image.load(resource_path("tileset/16bgpitch.png"))
bgpitch17 = pygame.image.load(resource_path("tileset/17bgpitch.png"))
bgpitch18 = pygame.image.load(resource_path("tileset/18bgpitch.png"))
bgpitch19 = pygame.image.load(resource_path("tileset/19bgpitch.png"))
bgpitch20 = pygame.image.load(resource_path("tileset/20bgpitch.png"))
bgpitch21 = pygame.image.load(resource_path("tileset/21bgpitch.png"))
bgpitch22 = pygame.image.load(resource_path("tileset/22bgpitch.png"))
bgpitch23 = pygame.image.load(resource_path("tileset/23bgpitch.png"))
bgpitch24 = pygame.image.load(resource_path("tileset/24bgpitch.png"))
bgpitch25 = pygame.image.load(resource_path("tileset/25bgpitch.png"))
bgpitch26 = pygame.image.load(resource_path("tileset/26bgpitch.png"))
bgpitch27 = pygame.image.load(resource_path("tileset/27bgpitch.png"))

bgpitches = {
    "1": bgpitch1,
    "2": bgpitch2,
    "3": bgpitch3,
    "4": bgpitch4,
    "5": bgpitch5,
    "6": bgpitch6,
    "7": bgpitch7,
    "8": bgpitch8,
    "9": bgpitch9,
    "10": bgpitch10,
    "11": bgpitch11,
    "12": bgpitch12,
    "13": bgpitch13,
    "14": bgpitch14,
    "15": bgpitch15,
    "16": bgpitch16,
    "17": bgpitch17,
    "18": bgpitch18,
    "19": bgpitch19,
    "20": bgpitch20,
    "21": bgpitch21,
    "22": bgpitch22,
    "23": bgpitch23,
    "24": bgpitch24,
    "25": bgpitch25,
    "26": bgpitch26,
    "27": bgpitch27,
}

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
#background.append(pygame.transform.scale(pygame.image.load("Fourier/bridge.png"), (2000, 900)))

wall = pygame.image.load(resource_path("statics/wall.png")).convert_alpha()
wall = pygame.transform.scale_by(wall, 2)

wall2 = pygame.image.load(resource_path("statics/middleplatform.png")).convert_alpha()
#wall2 = pygame.transform.scale_by(wall, 2)

bridge1 = pygame.image.load(resource_path("statics/bridge1.png")).convert_alpha()
bridge1 = pygame.transform.scale(bridge1, (150, 750))
bridge1 = pygame.transform.rotate(bridge1, 90)
bridge2 = pygame.image.load(resource_path("statics/bridge2.png")).convert_alpha()
bridge2 = pygame.transform.scale(bridge2, (150, 750))
bridge2 = pygame.transform.rotate(bridge2, 90)

platform = pygame.image.load(resource_path("statics/platform3.png")).convert_alpha()
platform = pygame.transform.scale(platform, (300, 100))

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
        
    for rect in draw_back:   
        i = str(rect[0])
        display.blit(bgpitches[i], (rect[1].x-camera.offset.x, rect[1].y-camera.offset.y))  
        #pygame.draw.rect(display, (0, 0, 255), (rect.x-camera.offset.x, rect.y-camera.offset.y, rect.width, rect.height))
        
    #draw rectangle
    for rect in foreground:  
        if type(rect)==type(pygame.rect.Rect()):
            display.blit(platform, (rect.x-camera.offset.x, rect.y-camera.offset.y))
            #pygame.draw.rect(display, (0, 0, 255), (rect.x-camera.offset.x, rect.y-camera.offset.y, rect.width, rect.height))
            DISPLAY_TILES.append(rect)
        elif type(rect)==type(()):
            if rect[1].w==384:
                display.blit(wall2, (rect[1].x-camera.offset.x, rect[1].y-camera.offset.y))
            elif rect[0]==-3:
                display.blit(bridge1, (rect[1].x-camera.offset.x, rect[1].y-camera.offset.y))
            elif rect[0]==-4:
                display.blit(bridge2, (rect[1].x-camera.offset.x, rect[1].y-camera.offset.y))
            else:
                display.blit(wall, (rect[1].x-camera.offset.x, rect[1].y-camera.offset.y))
            DISPLAY_TILES.append(rect[1])
        
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
    for m_tile in tiles:
        if type(m_tile)==type(()):
            if rect.colliderect(m_tile[1]):
                hit_list.append(m_tile[1])
        elif rect.colliderect(m_tile):
            hit_list.append(m_tile)
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