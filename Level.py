class Level:
    def __init__(self, foreground, game_map, level_inputs, level_setup):
        self.foreground = foreground
        self.game_map = game_map
        self.level_inputs = level_inputs
        self.level_setup = level_setup
        self.variables = {}
        
    def setup(self, camera):
        x = self.level_setup(self.foreground, camera)
        for arg in x:
            self.variables[arg[0]] = arg[1]
    
    def inputs(self, events):
        self.level_inputs(self.variables, events)