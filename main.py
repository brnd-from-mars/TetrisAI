# main.py


import tile
import gridController
import viewController


tile1 = tile.Tile( [ [1,0,0,0],[1,1,0,0],[1,0,0,0],[0,0,0,0] ], 1 )
tile2 = tile.Tile( [ [0,1,0,0],[0,1,0,0],[0,1,0,0],[0,1,0,0] ], 2 )
tile3 = tile.Tile( [ [0,0,0,0],[0,1,1,1],[0,1,0,0],[0,0,0,0] ], 3 )
tile4 = tile.Tile( [ [0,1,0,0],[1,1,1,1],[0,0,0,0],[0,0,0,0] ], 4 )
tile5 = tile.Tile( [ [0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0] ], 5 )
tile6 = tile.Tile( [ [1,1,0,0],[0,1,1,0],[0,0,0,0],[0,0,0,0] ], 6 )
tile7 = tile.Tile( [ [0,0,0,0],[0,1,1,0],[1,1,0,0],[0,0,0,0] ], 7 )


mTile = tile.MovableTile( tile2.layout, tile2.identifier )
mTile.incX()
mTile.incX()
mTile.incX()
mTile.incX()

mTile.incY()
mTile.incY()
mTile.incY()
mTile.incY()
mTile.incY()
mTile.incY()
mTile.incY()
mTile.incY()

mTile.rotCW()


gridController = gridController.GridController( )
viewController = viewController.ViewController( gridController )


while not viewController.abort:
    viewController.eventCheck( mTile )
    viewController.tileCheck( mTile )
    viewController.update( )
