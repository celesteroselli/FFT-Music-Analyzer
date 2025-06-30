import pygame
from physics import WINDOW_SIZE

class Level:
    def __init__(self, foreground, game_map, level_inputs, level_setup, level_dialogue, game_back, game_front):
        self.foreground = foreground
        self.game_map = game_map
        self.game_front = game_front
        self.game_back = game_back
        self.level_inputs = level_inputs
        self.level_setup = level_setup
        self.level_dialogue = level_dialogue
        self.variables = {}
        
    def setup(self, camera, startTime):
        x = self.level_setup(self.foreground, camera)
        for key, value in x.items():
            self.variables[key] = value
        self.variables["dialogue_on"] = False
        self.variables["new_dialogue"] = True
        self.variables["dialogue_count"] = 0
        self.variables["dialogue_box"] = pygame.Rect(100, WINDOW_SIZE[1]-100, WINDOW_SIZE[0]-200, 50)
        self.variables["write"] = ""
        self.variables["starttime"] = startTime
        self.variables["running"] = True
        self.variables["background"] = []
        self.variables["wrong"] = False
        
        self.variables["game_front"] = self.game_front
        self.variables["game_back"] = self.game_back
        
        self.variables["figure"] = False
        self.variables["last-note"] = 0
        self.variables["first_move"] = False

    def inputs(self, events, player):
        self.level_inputs(self.variables, events, player)
        
    def dialogue(self, player):
        return self.level_dialogue(self.variables, player)