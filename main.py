# main.py


import timeController
import scoreController
import gridController
import tileController
import viewController

import ai


timeController = timeController.TimeController( 1 )
scoreController = scoreController.ScoreController( )
gridController = gridController.GridController( scoreController )
tileController = tileController.TileController( gridController )
viewController = viewController.ViewController( gridController, timeController, scoreController )


cTile = tileController.getRandomTile( )
nTile = tileController.getRandomTile( )
viewController.setTile( cTile, nTile )


ai = ai.AI( gridController, viewController )


while not viewController.abort:
    move, rotate, rating =  ai.makeMove( cTile )
    print( rating )
    for i in range( 0, rotate ):
        cTile.rotCW( )
    if move<0:
        for i in range( 0, -move ):
            cTile.decX( )
    if move>0:
        for i in range( 0, move ):
            cTile.incX( )
    cTile.drop()

    if timeController.timeEvent( ):
        if not cTile.incY( ):
            cTile.apply( )
            scoreController.tileReleased( )
            gridController.checkForGameOver( )
            cTile = nTile
            nTile = tileController.getRandomTile( )
            viewController.setTile( cTile, nTile )
    viewController.updateEverything( )
