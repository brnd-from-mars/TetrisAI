# timeController.py


import time


class TimeController( object ):

    def __init__( self, interval ):
        self.eventInterval = interval
        self.lastTimedEvent = time.time( )
        self.speedMode = 3
        self.speedSet = [ 0.125, 0.25, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000]


    def getIntvProgress( self ):
        return ( time.time( ) - self.lastTimedEvent ) / ( self.eventInterval / self.speedSet[ self.speedMode ] )

    def incSpeed( self ):
        self.speedMode = min( self.speedMode+1, 14 )

    def decSpeed( self ):
        self.speedMode = max( self.speedMode-1, 0 )

    def getSpeed( self ):
        return self.speedSet[ self.speedMode ]

    def timeEvent( self ):
        if time.time( ) > self.lastTimedEvent + ( self.eventInterval / self.speedSet[ self.speedMode ] ):
            self.lastTimedEvent = time.time( )
            return True
        return False
