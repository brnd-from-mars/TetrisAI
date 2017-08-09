# ai.py


import population
import numpy as np


class AI( object ):

    def __init__( self, grid ):
        self.grid = grid
        self.population = population.Population( )
        self.currentGeneration = 0
        self.currentGenome = 0
        self.backupGrid = np.zeros( [ 10, 20 ], dtype=np.uint8 )
        self.backupTile = [ 0, 0, 0 ]

    def makeMove( self, tile ):
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

                if self.rateMove( )[ 0 ] > bestRating:
                    bestMove = move
                    bestRotate = rotate
                    bestRating, gameover = self.rateMove( )

                tile.psX, tile.psY, tile.rot = self.backupTile
                self.grid.grid = np.copy( self.backupGrid )

        self.grid.realAction = True
        self.grid.grid = np.copy( self.backupGrid )

        if gameover:
            if self.currentGenome == 19:
                self.currentGenome = 0
                self.population.generations[ self.currentGeneration ].genomes[ self.currentGenome ].score = score.getScore( )
                #self.currentGeneration += 1
            else:
                self.currentGenome += 1

        for i in range( 0, bestRotate ):
            tile.rotCW( )
        if bestMove<0:
            for i in range( 0, -bestMove ):
                tile.decX( )
        if bestMove>0:
            for i in range( 0, bestMove ):
                tile.incX( )
        tile.drop( )

        return bestMove, bestRotate, bestRating

    def rateMove( self ):
        gameover = False
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
            gameover = True
        return rating, gameover
