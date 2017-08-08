# tile.py


import numpy as np
import gridController


class Tile( object ):

    def __init__( self, layout, identifier):
        self.layout = np.array( layout, dtype=np.uint8 )
        self.identifier = identifier


class MovableTile( Tile ):

    def __init__( self, layout, identifier, grid ):
        Tile.__init__( self, layout, identifier )
        self.rot = 0
        self.psX = 0
        self.psY = 0
        self.grid = grid

    def incX( self ):
        rotated = np.rot90( self.layout, self.rot )
        for rowIndex in range( 4 ):
            row = rotated.T[ rowIndex ]
            lastBlock = -1
            for columnIndex in range( 4 ):
                if row[ columnIndex ] == 1:
                    lastBlock = columnIndex
            if lastBlock != -1:
                if not self.grid.checkField( self.psX + lastBlock + 1, self.psY + rowIndex ):
                    return False
        self.psX += 1
        return True

    def decX( self ):
        rotated = np.rot90( self.layout, self.rot )
        for rowIndex in range( 4 ):
            row = rotated.T[ rowIndex ]
            firstBlock = -1
            for columnIndex in range( 3, -1, -1 ):
                if row[ columnIndex ] == 1:
                    firstBlock = columnIndex
            if firstBlock != -1:
                if not self.grid.checkField( self.psX + firstBlock - 1, self.psY + rowIndex ):
                    return Fale
        self.psX -= 1
        return True

    def incY( self ):
        rotated = np.rot90( self.layout, self.rot )
        print()
        for columnIndex in range( 4 ):
            column = rotated[ columnIndex ]
            lowestBlock = -1
            for rowIndex in range( 4 ):
                if column[ rowIndex ] == 1:
                    lowestBlock = rowIndex
            if lowestBlock != -1:
                if not self.grid.checkField( self.psX + columnIndex, self.psY + lowestBlock + 1 ):
                    return False
        self.psY += 1
        return True

    def rotCW( self ):
        rotated = np.rot90( self.layout, ( self.rot + 1 ) % 4 )
        for x in range( 4 ):
            for y in range( 4 ):
                if rotated[ x, y ] == 1:
                    if not self.grid.checkField( self.psX + x, self.psY + y ):
                        return False
        self.rot = ( self.rot + 1 ) % 4
        return True

    def rotACW( self ):
        rotated = np.rot90( self.layout, ( self.rot -1 ) % 4 )
        for x in range( 4 ):
            for y in range( 4 ):
                if rotated[ x, y ] == 1:
                    if not self.grid.checkField( self.psX + x, self.psY + y ):
                        return False
        self.rot = ( self.rot - 1 ) % 4
        return True

    def render( self ):
        grid = np.zeros( [ 10, 20 ], dtype=np.uint8 )
        rotated = np.rot90( self.layout, self.rot)
        for x in range(4):
            for y in range(4):
                if -1 < x+self.psX < 10 and -1 < y+self.psY < 20:
                    grid[ x+self.psX, y+self.psY ] = rotated[ x, y ] * self.identifier
        return grid

class TileController( object ):

    def __init__( self ):
        self.tileSet = [
            Tile( [ [1,0,0,0],[1,1,0,0],[1,0,0,0],[0,0,0,0] ], 1 ),
            Tile( [ [0,1,0,0],[0,1,0,0],[0,1,0,0],[0,1,0,0] ], 2 ),
            Tile( [ [0,0,0,0],[0,1,1,1],[0,1,0,0],[0,0,0,0] ], 3 ),
            Tile( [ [0,1,0,0],[0,1,1,1],[0,0,0,0],[0,0,0,0] ], 4 ),
            Tile( [ [0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0] ], 5 ),
            Tile( [ [1,1,0,0],[0,1,1,0],[0,0,0,0],[0,0,0,0] ], 6 ),
            Tile( [ [0,0,0,0],[0,1,1,0],[1,1,0,0],[0,0,0,0] ], 7 )
        ]

    def getRandomTile( self ):
        pattern = self.tileSet[ np.random.random_integers( 6 ) ]
        return MovableTile( pattern.layout, pattern.identifier, gridController )
