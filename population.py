# population


import generation


class Population( object ):

    def __init__( self ):
        self.generation = [ generation.Generation( 0 ) ]
