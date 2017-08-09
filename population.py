# population


import generation


class Population( object ):

    def __init__( self ):
        self.generations = [ generation.Generation( 0 ) ]
        self.generations[ 0 ].initialGeneration( )
