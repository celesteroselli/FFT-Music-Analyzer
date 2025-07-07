import pygame
from Fourier.physics import *
import time
#from Fourier.Level1 import TILE_RECTS, collision_test

idlesprites = ["tileset/char000.png", "tileset/char001.png"]

class PlayerClass(pygame.sprite.Sprite):
    COLOR = (255, 0, 0)
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.colliding = False
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.animate = "idle"
        self.start = time.perf_counter()
        self.spriteurl = "Fourier/tileset/0.png"
        self.idlesprites = ["Fourier/tileset/char000.png", "Fourier/tileset/char001.png"]
        self.runsprites = ["Fourier/tileset/char025.png", "Fourier/tileset/char026.png", "Fourier/tileset/char027.png", "Fourier/tileset/char028.png", "Fourier/tileset/char029.png", "Fourier/tileset/char030.png", "Fourier/tileset/char031.png", "Fourier/tileset/char032.png"]
        self.jumpsprites = ["Fourier/tileset/char041.png", "Fourier/tileset/char042.png", "Fourier/tileset/char043.png", "Fourier/tileset/char044.png", "Fourier/tileset/char045.png", "Fourier/tileset/char046.png", "Fourier/tileset/char047.png", "Fourier/tileset/char048.png"]
        self.i = 0
        self.ticker = 0.7
        self.facing = 0
        
    def is_colliding(self):
        return self.colliding
        
    def set_colliding(self, var):
        self.colliding = var
        
    def move(self, dx, dy, m_list):
        #process x-axis
        self.rect.x += dx
        
        hit_list = collision_test(self.rect, m_list)
        for tile in hit_list:
            if dx > 0:
                self.rect.right = tile.left
            if dx < 0:
                self.rect.left = tile.right
                
        self.set_colliding(False)
        
        #process y-axis
        self.rect.y += dy
        hit_list = collision_test(self.rect, m_list)
        for tile in hit_list:
            self.set_colliding(True)
            if dy > 0:
                self.rect.bottom = tile.top
            if dy < 0:
                self.rect.top = tile.bottom
                
    def kill(self, camera):
        camera.offset.x = 0
        camera.offset.y = 0
        self.rect.x = PLAYER_SCREEN_OFFSET
        self.rect.y = 1600
        
    def move_x(self, vel):
        self.x_vel = vel
        
    def move_y(self, vel):
        self.y_vel = vel

    def doAnimation(self):
        if (time.perf_counter() - self.start)>=self.ticker:
            self.i = self.i+1
            self.start = time.perf_counter()
        match self.animate:
            case "idle":
                if self.i >= len(self.idlesprites):
                    self.i = 0
                self.sprite = pygame.transform.scale(pygame.image.load(self.idlesprites[self.i]), (self.rect.w, self.rect.h))
            case "move":
                if self.i >= len(self.runsprites):
                    self.i = 0
                self.sprite = pygame.transform.scale(pygame.image.load(self.runsprites[self.i]), (self.rect.w, self.rect.h))
            case "jump":
                if self.i >= len(self.jumpsprites):
                    self.i = 0
                self.sprite = pygame.transform.scale(pygame.image.load(self.jumpsprites[self.i]), (self.rect.w, self.rect.h))
            case _:
                if self.i >= len(self.idlesprites):
                    self.i = 0
                self.sprite = self.idlesprites[self.i]
        
    def draw(self, win, camera):
        self.doAnimation()
        if self.facing==1:
            self.sprite = pygame.transform.flip(self.sprite, True, False)
        display.blit(self.sprite, (self.rect.x-camera.offset.x, self.rect.y-camera.offset.y))
        #pygame.draw.rect(win, self.COLOR, (self.rect.x-camera.offset.x, self.rect.y-camera.offset.y, self.rect.width, self.rect.height))

def handle_move(player):
    key = pygame.key.get_pressed()
    
    player.x_vel = 0
    if key[pygame.K_LEFT]:
        player.animate = "move"
        player.facing = 1
        player.ticker = 0.1
        player.move_x(-6.5)
    if key[pygame.K_RIGHT]:
        player.animate = "move"
        player.facing = 0
        player.ticker = 0.1
        player.move_x(6.5)
    if key[pygame.K_UP]:
        if (player.is_colliding() == True):
            player.move_y(-6)
            player.set_colliding(False)
    if (not key[pygame.K_LEFT]) and (not key[pygame.K_RIGHT]) and (not key[pygame.K_UP]):
        player.animate = "idle"
        player.ticker = 0.7
        
