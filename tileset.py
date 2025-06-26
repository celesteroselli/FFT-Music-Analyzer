
import pandas as pd
import numpy as np
import pygame
def go(name):
    df = pd.read_csv(f"tilemaps/{name}.csv")
    nparray = df.to_numpy()
    array_shape = nparray.shape
    coolarray = []
    for i in range((array_shape[0])):
        coolarray.append([])
        for tile in nparray[i]:
            coolarray[i].append(tile)
    return coolarray

def images(size):
    # dict = {
    #     "0": pygame.transform.scale(pygame.image.load("tileset/0.png"), (size, size)),
    #     "1": pygame.transform.scale(pygame.image.load("tileset/1.png"), (size, size)),
    #     "2": pygame.transform.scale(pygame.image.load("tileset/2.png"), (size, size)),
    #     "3": pygame.transform.scale(pygame.image.load("tileset/3.png"), (size, size)),
    #     "4": pygame.transform.scale(pygame.image.load("tileset/4.png"), (size, size)),
    #     "5": pygame.transform.scale(pygame.image.load("tileset/5.png"), (size, size)),
    #     "10": pygame.transform.scale(pygame.image.load("tileset/10.png"), (size, size)),
    #     "11": pygame.transform.scale(pygame.image.load("tileset/11.png"), (size, size)),
    # }
    dict = {}
    for i in range(23-1):
        dict[f"{i}"] = pygame.transform.scale(pygame.image.load(f"tileset/{i}.png"), (size, size))
    return dict