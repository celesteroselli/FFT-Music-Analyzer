import pygame
import os
import sys

global USER_CHORD_MIN
USER_CHORD_MIN = 150
global USER_CHORD_MAX
USER_CHORD_MAX = 700
global OCTAVE
OCTAVE = 0.5

def change_octave(change):
    global OCTAVE
    OCTAVE = change
    
    match change:
        
        case 0.25:
            global USER_CHORD_MIN
            global USER_CHORD_MAX
            USER_CHORD_MIN = 75
            USER_CHORD_MAX = 350
            
        case 0.5:
            USER_CHORD_MIN = 150
            USER_CHORD_MAX = 700
            
        case 1:
            USER_CHORD_MIN = 300
            USER_CHORD_MAX = 1400

def get_octave():
    return OCTAVE

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS  # this is the temp folder PyInstaller uses
        print(base_path)
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

pitch_data = {
    "Pitch": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    "Frequency": [261.63, 277.18, 293.66, 311.13, 329.63, 349.23, 369.99, 392.00, 415.30, 440.00, 466.16, 493.88, 523.25],
    "Note": ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B", "C"]
}

pygame.font.init() # you have to call this at the starsst, 
font_path = resource_path("tileset/PixelifySans-Regular.ttf")
my_font = pygame.font.Font(font_path, 36)
title_font = pygame.font.Font(font_path, 55)

color1 = (160,0,68)
color2 = (32,42,120)
color3 = (161,181,232)