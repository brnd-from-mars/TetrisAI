# main.py


import gridController
import viewController


gridController = gridController.GridController( )
viewController = viewController.ViewController( gridController )


while not viewController.abort:
    viewController.eventCheck( )
    viewController.update( )
