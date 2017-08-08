# generation.py


import genome


class Generation( object ):

    def __init__( self, generation ):
        self.generation = generation
        self.genomes = 50 * [ genome.Genome( ) ]
