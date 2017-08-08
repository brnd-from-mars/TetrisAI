# tile.py


import numpy as np


class Tile( object ):

    def __init__( self, layout, identifier):
        self.layout = np.array( layout, dtype=np.uint8 )
        self.identifier = identifier


class MovableTile( Tile ):

    def __init__( self, layout, identifier ):
        Tile.__init__( self, layout, identifier )
        self.rot = 0
        self.psX = 0
        self.psY = 0

    def incX( self ):
        self.psX += 1

    def decX( self ):
        self.psX -= 1

    def incY( self ):
        self.psY += 1

    def rotCW( self ):
        self.rot = ( self.rot + 1 ) % 4

    def rotACW( self ):
        self.rot = ( self.rot + 3 ) % 4

    def render( self ):
        grid = np.zeros( [ 10, 20 ], dtype=np.uint8 )
        rotated = np.rot90( self.layout, self.rot)
        for x in range(4):
            for y in range(4):
                if -1 < x+self.psX < 10 and -1 < y+self.psY < 20:
                    grid[ x+self.psX, y+self.psY ] = rotated[ x, y ]
        return grid
