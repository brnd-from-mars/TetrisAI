# gridController.py


import numpy as np


class GridController( object ):

    def __init__( self ):
        self.grid = np.zeros( [ 10, 20 ], dtype=np.uint8 )
