import pygame

USER_CHORD_MIN = 100
USER_CHORD_MAX = 600

OCTAVE = 1

pitch_data = {
    "Pitch": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    "Frequency": [261.63, 277.18, 293.66, 311.13, 329.63, 349.23, 369.99, 392.00, 415.30, 440.00, 466.16, 493.88, 523.25],
    "Note": ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B", "C"]
}

pygame.font.init() # you have to call this at the start, 
my_font = pygame.font.SysFont('Comic Sans MS', 30)