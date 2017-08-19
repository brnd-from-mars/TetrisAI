# population


import generation
import numpy as np


class Population( object ):

    def __init__( self ):
        self.generations = [ generation.Generation( 0 ) ]
        self.generations[ 0 ].initialGeneration( )

    def nextGen( self ):
        cGen = len( self.generations )-1
        nGen = cGen + 1

        scores = []
        i = 0
        for genome in self.generations[ cGen ].genomes:
            scores.append( ( i, genome.score ) )
            i+=1

        scores = np.sort( np.array( scores, dtype=[ ( 'index', int ), ( 'score', int ) ] ), order='score' )

        elite = list( reversed( [ x[ 0 ] for x in scores[ 30:40 ] ] ) )

        self.generations[ cGen ].elite = elite

        self.generations.append( generation.Generation( nGen ) )

        for i in range( 40 ):
            if i<5:
                self.generations[ nGen ].genomes[ i ].cross( self.generations[ cGen ].genomes[ elite[ i ] ], self.generations[ cGen ].genomes[ elite[ i ] ] )
            else:
                mum = np.random.randint( 10 )
                dad = np.random.randint( 10 )
                self.generations[ nGen ].genomes[ i ].cross( self.generations[ cGen ].genomes[ elite[ mum ] ], self.generations[ cGen ].genomes[ elite[ dad ] ] )
            self.generations[ nGen ].genomes[ i ].mutate(  )
