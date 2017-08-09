# gridController.py


import numpy as np
import math


class GridController( object ):

    def __init__( self, score ):
        self.score = score
        self.grid = np.zeros( [ 10, 20 ], dtype=np.uint8 )
        self.realAction = True
        self.lastRowsCleared = 0
        self.lastMaxHeight = 0
        self.lastSumHeight = 0
        self.lastRelativeHeight = 0
        self.lastRoughness = 0
        self.lastAmountHoles = 0


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
        self.lastRowsCleared = rows
        heightData = [ ]
        for column in self.grid:
            counter = 20
            for i in range(19, -1, -1):
                if column[i] != 0:
                    counter = i
            heightData.append( 20-counter )
        self.lastMaxHeight = np.amax( heightData )
        self.lastSumHeight = np.sum( heightData )
        self.lastRelativeHeight = self.lastMaxHeight - np.amin( heightData )
        self.lastRoughness = 0
        for x in range( 9 ):
            self.lastRoughness += abs( heightData[ x ] + heightData[ x-1 ] )
        self.lastAmountHoles = 0
        for x in range( 10 ):
            for y in range( 19, 1, -1 ):
                if self.grid[ x, y ] == 0 and self.grid[ x, y-1 ] != 0:
                    self.lastAmountHoles += 1
        if self.realAction:
            self.score.rowsCleared( rows )

    def checkForGameOver( self ):
        for y in range( 4 ):
            if np.amax( self.grid.T[ y ] ) != 0:
                if self.realAction:
                    self.reset( )
                return True
        return False

    def reset( self ):
        self.grid = np.zeros( [ 10, 20 ], dtype=np.uint8 )
        if self.realAction:
            self.score.reset( )
