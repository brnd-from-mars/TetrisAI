# main.py


import tile
import gridController
import viewController


gridController = gridController.GridController( )
viewController = viewController.ViewController( gridController )


tile1 = tile.Tile( [ [0,1,0,0],[1,1,1,0],[0,0,0,0],[0,0,0,0] ], 1 )
tile2 = tile.Tile( [ [0,0,0,0],[1,1,1,1],[0,0,0,0],[0,0,0,0] ], 2 )
tile3 = tile.Tile( [ [0,0,0,0],[0,1,1,0],[0,1,0,0],[0,1,0,0] ], 3 )
tile4 = tile.Tile( [ [0,0,0,0],[1,1,0,0],[0,1,0,0],[0,0,0,0] ], 4 )
tile5 = tile.Tile( [ [0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0] ], 5 )
tile6 = tile.Tile( [ [0,1,1,0],[1,1,0,0],[0,0,0,0],[0,0,0,0] ], 6 )
tile7 = tile.Tile( [ [1,1,0,0],[0,1,1,0],[0,0,0,0],[0,0,0,0] ], 7 )


while not viewController.abort:
    viewController.eventCheck( )
    viewController.update( )
