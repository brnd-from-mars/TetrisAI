# gridController.py


import numpy as np


class GridController( object ):

    def __init__( self ):
        self.grid = np.zeros( [ 10, 20 ], dtype=np.uint8 )
        for y in range( 14, 20 ):
            for x in range( 10 ):
                if not 3 < x < 8:
                    self.grid[ x, y ] = 3


    def checkField( self, psX, psY ):
        if psX > 9:
            return False
        if psX < 0:
            return False
        if psY > 19:
            return False
        if psY < 0:
            return False
        if self.grid[ psX, psY ] != 0:
            return False
        return True
