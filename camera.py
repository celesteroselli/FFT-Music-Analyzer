import pygame
from physics import TILE_SIZE, GROUND_ROWS, PLAYER_SCREEN_OFFSET

vec = pygame.math.Vector2
from abc import ABC, abstractmethod

class Camera:
    def __init__(self, player):
        self.offset = vec(0,0)
        self.offset_float = vec(0,0)
        self.DISPLAY_W, self.DISPLAY_H = 1500,900
        self.CONST = vec(-PLAYER_SCREEN_OFFSET, -297)
        
class CamScroll:
    def __init__(self, camera, player):
       self.camera = camera
       self.player = player
       
    def scroll(self):
        self.camera.offset_float.x += (self.player.rect.x - self.camera.offset_float.x + self.camera.CONST.x)
        #equals not +=
        if (self.player.rect.y < 300):
            self.camera.offset_float.y += (self.player.rect.y - self.camera.offset_float.y + self.camera.CONST.y)
        else:
            self.camera.offset_float.y += 0
        self.camera.offset.x = int(self.camera.offset_float.x)
        self.camera.offset.y = int(self.camera.offset_float.y)