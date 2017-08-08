# gridController.py


import numpy as np


class GridController( object ):

    def __init__( self, score ):
        self.score = score
        self.grid = np.zeros( [ 10, 20 ], dtype=np.uint8 )
        for y in range( 14, 20 ):
            for x in range( 10 ):
                if not 3 < x < 8:
                    self.grid[ x, y ] = 3


    def checkField( self, psX, psY ):
        if psX < 0 or psX > 9 or psY > 19 or psY < 0:
            return False
        if self.grid[ psX, psY ] != 0:
            return False
        return True

    def apply( self, posX, posY, identifier ):
        self.grid[ posX, posY ] = identifier

    def removeCompleteRows( self ):
        rows = 0
        for y in range( 19, -1, -1 ):
            while np.amin( self.grid.T[ y ] ) != 0:
                rows += 1
                for y2 in range( y, 0, -1 ):
                    for x in range( 10 ):
                        self.grid[ x, y2 ] = self.grid[ x, y2-1 ]
        self.score.rowsCleared( rows )

    def checkForGameOver( self ):
        for y in range( 4 ):
            if np.amax( self.grid.T[ y ] ) != 0:
                self.reset( )

    def reset( self ):
        self.grid = np.zeros( [ 10, 20 ], dtype=np.uint8 )
        self.score.reset( )
