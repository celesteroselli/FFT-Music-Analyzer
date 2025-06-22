import pygame
from physics import *
#from level1 import TILE_RECTS, collision_test

class PlayerClass(pygame.sprite.Sprite):
    COLOR = (255, 0, 0)
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.colliding = False
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        
    def is_colliding(self):
        return self.colliding
        
    def set_colliding(self, var):
        self.colliding = var
        
    def move(self, dx, dy):
        COLLIDING = False
        #process x-axis
        self.rect.x += dx
        hit_list = collision_test(self.rect, TILE_RECTS)
        for tile in hit_list:
            if dx > 0:
                self.rect.right = tile.left
            if dx < 0:
                self.rect.left = tile.right
                
        #process y-axis
        self.rect.y += dy
        hit_list = collision_test(self.rect, TILE_RECTS)
        for tile in hit_list:
            self.set_colliding(True)
            if dy > 0:
                self.rect.bottom = tile.top
            if dy < 0:
                self.rect.top = tile.bottom
        
    def move_x(self, vel):
        self.x_vel = vel
        
    def move_y(self, vel):
        self.y_vel = vel
        
    def loop(self):
        #do gravity if not colliding with a floor
        if (self.is_colliding() == False):
           self.y_vel = self.y_vel + 0.1
           print("doing gravity " + str(self.y_vel))
        self.move(self.x_vel, self.y_vel)
        
    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, self.rect)

def handle_move(player):
    key = pygame.key.get_pressed()
    
    player.x_vel = 0
    if key[pygame.K_LEFT]:
        player.move_x(-1)
    if key[pygame.K_RIGHT]:
        player.move_x(1)
    if key[pygame.K_UP]:
        if (player.is_colliding() == True):
            player.move_y(-2)
            player.set_colliding(False)
            print("moving up")