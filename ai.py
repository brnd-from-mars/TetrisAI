# ai.py


import population
import numpy as np


class AI( object ):

    def __init__( self, grid, view ):
        self.grid = grid
        self.view = view
        self.population = population.Population( )
        self.currentGeneration = 0
        self.currentGenome = 0
        self.backupGrid = np.zeros( [ 10, 20 ], dtype=np.uint8 )
        self.backupTile = [ 0, 0, 0 ]

    def makeMove( self, tile ):
        self.view.setUpdate( False )
        self.backupGrid = np.copy( self.grid.grid )
        self.grid.realAction = False
        self.backupTile = [ tile.psX, tile.psY, tile.rot ]

        bestRating = -10000000000000
        bestMove = 0
        bestRotate = 0

        for move in range( -5, 6 ):
            for rotate in range( 0, 3 ):
                for i in range( 0, rotate ):
                    tile.rotCW( )
                if move<0:
                    for i in range( 0, -move ):
                        tile.decX( )
                if move>0:
                    for i in range( 0, move ):
                        tile.incX( )
                tile.drop( )
                tile.apply( )
                self.grid.removeCompleteRows( )

                if self.rateMove( ) > bestRating:
                    bestMove = move
                    bestRotate = rotate
                    bestRating = self.rateMove( )

                tile.psX, tile.psY, tile.rot = self.backupTile
                self.grid.grid = np.copy( self.backupGrid )

        self.grid.realAction = True
        self.grid.grid = np.copy( self.backupGrid )
        self.view.setUpdate( True )

        return bestMove, bestRotate, bestRating

    def rateMove( self ):
        cGenome = self.population.generations[ self.currentGeneration ].genomes[ self.currentGenome ]
        rating = 0
        rating += self.grid.lastRowsCleared * cGenome.weightRowsCleared
        rating += self.grid.lastMaxHeight * cGenome.weightMaxHeight
        rating += self.grid.lastSumHeight * cGenome.weightSumHeight
        rating += self.grid.lastRelativeHeight * cGenome.weightRelativeHeight
        rating += self.grid.lastAmountHoles * cGenome.weightAmountHoles
        rating += self.grid.lastRoughness * cGenome.weightRoughness
        if self.grid.checkForGameOver( ):
            rating -= 500
        return rating
