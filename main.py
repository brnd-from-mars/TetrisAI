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
viewController = viewController.ViewController( gridController, timeController )


tile = tileController.getRandomTile(  )
viewController.setTile( tile )


while not viewController.abort:
    print( scoreController.getScore( ) )
    if timeController.timeEvent( ):
        if not tile.incY():
            tile.apply( )
            scoreController.tileReleased( )
            gridController.checkForGameOver( )
            tile = tileController.getRandomTile(  )
            viewController.setTile( tile )
    viewController.update( )
