# main.py


import timeController
import scoreController
import gridController
import tileController

import grapher

import ai

import viewController


timeController = timeController.TimeController( 1 )
scoreController = scoreController.ScoreController( )
gridController = gridController.GridController( scoreController )
tileController = tileController.TileController( gridController )

grapher = grapher.Grapher( scoreController )

ai = ai.AI( gridController, scoreController, grapher )

viewController = viewController.ViewController( gridController, timeController, scoreController, ai, grapher )


cTile = tileController.getRandomTile( )
nTile = tileController.getRandomTile( )
viewController.setTile( cTile, nTile )


while not viewController.abort:
    if timeController.timeEvent( ):
        if viewController.aiState:
            move, rotate, rating =  ai.makeMove( cTile )
        if not cTile.incY( ):
            cTile.apply( )
            if not gridController.checkForGameOver( ):
                scoreController.tileReleased( )
            cTile = nTile
            nTile = tileController.getRandomTile( )
            viewController.setTile( cTile, nTile )
    viewController.updateEverything( )
