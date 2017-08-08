# main.py


import tile
import gridController
import viewController


tileController = tile.TileController()
gridController = gridController.GridController( )
viewController = viewController.ViewController( gridController )


mTile = tileController.getRandomTile(  )


while not viewController.abort:
    viewController.eventCheck( mTile )
    viewController.tileCheck( mTile )
    viewController.update( )
