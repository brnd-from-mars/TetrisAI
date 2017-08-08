# main.py


import tileController
import gridController
import viewController


gridController = gridController.GridController( )
tileController = tileController.TileController( gridController )
viewController = viewController.ViewController( gridController )


Tile = tileController.getRandomTile(  )


while not viewController.abort:
    viewController.eventCheck( Tile )
    viewController.tileCheck( Tile )
    viewController.update( )
