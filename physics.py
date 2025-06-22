import pygame

screen = pygame.display.set_mode([1500, 900])
WINDOW_SIZE = screen.get_size()
DISPLAY_SIZE = (WINDOW_SIZE[0] / 5, WINDOW_SIZE[1] / 5)
print(DISPLAY_SIZE)
TILE_SIZE = 30

image = pygame.image.load("image.png")
game_map = [
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1'],
]

display = pygame.Surface(DISPLAY_SIZE)
TILE_RECTS = []
def draw_background():
    display.fill((255, 255, 255))
    y=0
    for row in game_map:
        x=0
        for tile in row:
            if tile == "1":
                display.blit(image, (x*TILE_SIZE, y*TILE_SIZE))
                TILE_RECTS.append(pygame.Rect(x * TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE))
            x += 1
        y += 1
        
def collision_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list