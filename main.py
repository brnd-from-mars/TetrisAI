# main.py


import timeController
import scoreController
import gridController
import tileController
import viewController

import genome


timeController = timeController.TimeController( 1 )
scoreController = scoreController.ScoreController( )
gridController = gridController.GridController( scoreController )
tileController = tileController.TileController( gridController )
viewController = viewController.ViewController( gridController, timeController, scoreController )


cTile = tileController.getRandomTile( )
nTile = tileController.getRandomTile( )
viewController.setTile( cTile, nTile )


A = genome.Genome()
A.initialGenome()
B = genome.Genome()
B.initialGenome()
C = genome.Genome()
C.cross(A, B)

print(A)
print(B)
print(C)


while not viewController.abort:
    if timeController.timeEvent( ):
        if not cTile.incY( ):
            cTile.apply( )
            scoreController.tileReleased( )
            gridController.checkForGameOver( )
            cTile = nTile
            nTile = tileController.getRandomTile( )
            viewController.setTile( cTile, nTile )
    viewController.update( )
