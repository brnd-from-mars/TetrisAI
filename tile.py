# tile.py


import numpy as np


class Tile( object ):

    def __init__( self, _layout, _identifier, _posX=0, _posY=0, _rot=0 ):
        self.layout = np.array( _layout )
        self.identifier = _identifier
        self.posX = _posX
        self.posY = _posY
        self.rot = _rot
