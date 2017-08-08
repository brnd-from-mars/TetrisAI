# main.py


import timeController
import gridController
import tileController
import viewController


timeController = timeController.TimeController( 1 )
gridController = gridController.GridController( )
tileController = tileController.TileController( gridController )
viewController = viewController.ViewController( gridController )


Tile = tileController.getRandomTile(  )


while not viewController.abort:
    if timeController.timeEvent( ):
        if not Tile.incY():
            Tile.apply( )
            Tile = tileController.getRandomTile(  )
            gridController.removeCompleteRows( )
    viewController.eventCheck( Tile )
    viewController.tileCheck( Tile )
    viewController.timeCheck( timeController )
    viewController.update( )
