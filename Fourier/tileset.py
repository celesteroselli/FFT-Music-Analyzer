
import pandas as pd
import numpy as np
import pygame
from Fourier.usersettings import resource_path

def go(name):
    path = resource_path(f"tilemaps/{name}.csv")
    df = pd.read_csv(path)
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
        path = resource_path(f"tileset/{i}.png")
        dict[f"{i}"] = pygame.transform.scale(pygame.image.load(path), (size, size))
    return dict