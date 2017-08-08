# ai.py


import population


class AI( object ):

    def __init__( self, grid, view ):
        self.grid = grid
        self.view = view
        self.population = population.Population()
        self.currentGeneration = 0
