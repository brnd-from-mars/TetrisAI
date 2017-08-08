# main.py


import tile
import gridController
import viewController


gridController = gridController.GridController( )
viewController = viewController.ViewController( gridController )


tileSet = [ tile.Tile( [ [1,0,0,0],[1,1,0,0],[1,0,0,0],[0,0,0,0] ], 1 ),
            tile.Tile( [ [0,1,0,0],[0,1,0,0],[0,1,0,0],[0,1,0,0] ], 2 ),
            tile.Tile( [ [0,0,0,0],[0,1,1,1],[0,1,0,0],[0,0,0,0] ], 3 ),
            tile.Tile( [ [0,1,0,0],[1,1,1,1],[0,0,0,0],[0,0,0,0] ], 4 ),
            tile.Tile( [ [0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0] ], 5 ),
            tile.Tile( [ [1,1,0,0],[0,1,1,0],[0,0,0,0],[0,0,0,0] ], 6 ),
            tile.Tile( [ [0,0,0,0],[0,1,1,0],[1,1,0,0],[0,0,0,0] ], 7 ) ]


mTile = tile.MovableTile( tileSet[6].layout, tileSet[6].identifier, gridController )


while not viewController.abort:
    viewController.eventCheck( mTile )
    viewController.tileCheck( mTile )
    viewController.update( )
