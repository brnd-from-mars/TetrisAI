# main.py


import timeController
import scoreController
import gridController
import tileController

import ai

import viewController


timeController = timeController.TimeController( 1 )
scoreController = scoreController.ScoreController( )
gridController = gridController.GridController( scoreController )
tileController = tileController.TileController( gridController )

ai = ai.AI( gridController, scoreController )

viewController = viewController.ViewController( gridController, timeController, scoreController, ai )


cTile = tileController.getRandomTile( )
nTile = tileController.getRandomTile( )
viewController.setTile( cTile, nTile )


while not viewController.abort:
    if timeController.timeEvent( ):
        move, rotate, rating =  ai.makeMove( cTile )
        if not cTile.incY( ):
            cTile.apply( )
            if not gridController.checkForGameOver( ):
                scoreController.tileReleased( )
            cTile = nTile
            nTile = tileController.getRandomTile( )
            viewController.setTile( cTile, nTile )
    viewController.updateEverything( )
