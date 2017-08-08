# main.py


import timeController
import gridController
import tileController
import viewController


timeController = timeController.TimeController( 1 )
gridController = gridController.GridController( )
tileController = tileController.TileController( gridController )
viewController = viewController.ViewController( gridController, timeController )


Tile = tileController.getRandomTile(  )
viewController.setTile( Tile )


while not viewController.abort:
    if timeController.timeEvent( ):
        if not Tile.incY():
            Tile.apply( )
            Tile = tileController.getRandomTile(  )
            viewController.setTile( Tile )
    viewController.update( )
