# main.py


import timeController
import scoreController
import gridController
import tileController
import viewController


timeController = timeController.TimeController( 1 )
scoreController = scoreController.ScoreController( )
gridController = gridController.GridController( scoreController )
tileController = tileController.TileController( gridController )
viewController = viewController.ViewController( gridController, timeController, scoreController )


cTile = tileController.getRandomTile( )
nTile = tileController.getRandomTile( )
viewController.setTile( cTile, nTile )


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
