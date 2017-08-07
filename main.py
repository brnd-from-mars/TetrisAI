# main.py


import viewController


viewController = viewController.ViewController( )


while not viewController.abort:
    viewController.eventCheck( )
    viewController.update( )
