
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

def images():
    dict = {
        "0": pygame.transform.smoothscale(pygame.image.load("tileset/0.png"), (32, 32)),
        "1": pygame.transform.smoothscale(pygame.image.load("tileset/1.png"), (32, 32)),
        "2": pygame.transform.smoothscale(pygame.image.load("tileset/2.png"), (32, 32)),
        "3": pygame.transform.smoothscale(pygame.image.load("tileset/3.png"), (32, 32)),
        "4": pygame.transform.smoothscale(pygame.image.load("tileset/4.png"), (32, 32)),
        "5": pygame.transform.smoothscale(pygame.image.load("tileset/5.png"), (32, 32)),
        "10": pygame.transform.smoothscale(pygame.image.load("tileset/10.png"), (32, 32)),
        "11": pygame.transform.smoothscale(pygame.image.load("tileset/11.png"), (32, 32)),
    }
    return dict