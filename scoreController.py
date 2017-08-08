# scoreController.py


class ScoreController( object ):

    def __init__( self ):
        self.score = 0
        self.highest = 0
        self.clearPoints = [ 0, 40, 100, 300, 1200 ]

    def rowsCleared( self, rows ):
        self.score += self.clearPoints[ rows ]

    def tileReleased( self ):
        self.score += 10

    def getScore( self ):
        return self.score

    def getHighscore( self ):
        return self.highest

    def reset( self ):
        if self.score > self.highest:
            self.highest = self.score
        self.score = 0
