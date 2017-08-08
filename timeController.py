# timeController.py


import time


class TimeController( object ):

    def __init__( self, interval ):
        self.eventInterval = interval
        self.lastTimedEvent = time.time( )


    def getIntvProgress( self ):
        return ( time.time( ) - self.lastTimedEvent ) / self.eventInterval

    def timeEvent( self ):
        if time.time( ) > self.lastTimedEvent + self.eventInterval:
            self.lastTimedEvent = time.time( )
            return True
        return False
