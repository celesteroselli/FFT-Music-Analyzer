import pygame

vec = pygame.math.Vector2
from abc import ABC, abstractmethod

class Camera:
    def __init__(self, player):
        self.offset = vec(0,0)
        self.offset_float = vec(0,0)
        self.DISPLAY_W, self.DISPLAY_H = 500,300
        self.CONST = vec(-250, -100)
        
class CamScroll:
    def __init__(self, camera, player):
       self.camera = camera
       self.player = player
       
    def scroll(self):
        self.camera.offset_float.x += (self.player.rect.x - self.camera.offset_float.x + self.camera.CONST.x)
        self.camera.offset.x = int(self.camera.offset_float.x)