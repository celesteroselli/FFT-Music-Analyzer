class Level:
    def __init__(self, foreground, game_map, level_inputs, level_setup):
        self.foreground = foreground
        self.game_map = game_map
        self.level_inputs = level_inputs
        self.level_setup = level_setup
        self.variables = {}
        
    def setup(self):
        x = self.level_setup()
        for arg in x:
            self.variables[x[0]] = x[1]
    
    def inputs(self, camera):
        self.level_inputs(self.variables, self.foreground, camera)