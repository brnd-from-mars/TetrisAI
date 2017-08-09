# generation.py


import genome


class Generation( object ):

    def __init__( self, generation ):
        self.generation = generation
        self.genomes = []
        for i in range( 20 ):
            self.genomes.append( genome.Genome( self.generation ) )


    def __str__( self ):
        output = '\nGeneration: ' + str( self.generation )
        for i in range( 20 ):
            output += '\n Genom ' + str( i ) + '; ID: ' + str( self.genomes[i].identifier ) + '; Score: ' + str(  self.genomes[i].score  )
        return output

    def initialGeneration( self ):
        for genome in self.genomes:
            genome.initialGenome( )

    __repr__ = __str__
