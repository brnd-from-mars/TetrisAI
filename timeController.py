# timeController.py


import time


class TimeController( object ):

    def __init__( self, interval ):
        self.eventInterval = interval
        self.lastTimedEvent = time.time( )
        self.speed = 1


    def getIntvProgress( self ):
        return ( time.time( ) - self.lastTimedEvent ) / self.eventInterval

    def incSpeed( self ):
        self.eventInterval /= 2
        self.speed *= 2

    def decSpeed( self ):
        self.eventInterval *= 2
        self.speed /= 2

    def getSpeed( self ):
        return self.speed

    def timeEvent( self ):
        if time.time( ) > self.lastTimedEvent + self.eventInterval:
            self.lastTimedEvent = time.time( )
            return True
        return False
