
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
    dict = {}
    for i in range(23-1):
        dict[f"{i}"] = pygame.transform.scale(pygame.image.load(f"tileset/{i}.png"), (size, size))
    return dict