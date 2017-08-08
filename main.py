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


Tile = tileController.getRandomTile(  )
viewController.setTile( Tile )


while not viewController.abort:
    print( scoreController.getScore( ) )
    if timeController.timeEvent( ):
        if not Tile.incY():
            scoreController.tileReleased( )
            Tile.apply( )
            Tile = tileController.getRandomTile(  )
            viewController.setTile( Tile )
    viewController.update( )
