# genome.py


import numpy as np
from random import choice


class Genome( object ):

    def __init__( self, generation ):
        self.identifier           = np.random.random( )
        self.weightRowsCleared    = 0
        self.weightMaxHeight      = 0
        self.weightSumHeight      = 0
        self.weightRelativeHeight = 0
        self.weightAmountHoles    = 0
        self.weightRoughness      = 0
        self.mutationRate         = 0.05
        self.mutationStep         = 0.2
        self.generation           = generation
        self.mum                  = None
        self.dad                  = None
        self.score                = 0

    def __str__( self ):
        output  =   'Score      : ' + str( self.score      )
        output += '\nIdentifier : ' + str( self.identifier )
        output += '\nMum        : ' + str( self.mum        )
        output += '\nDad        : ' + str( self.dad        )
        output += '\n -wRowsCleared    : %0.10f' % self.weightRowsCleared
        output += '\n -wMaxHeight      : %0.10f' % self.weightMaxHeight
        output += '\n -wSumHeight      : %0.10f' % self.weightSumHeight
        output += '\n -wRelativeHeight : %0.10f' % self.weightRelativeHeight
        output += '\n -wAmountHoles    : %0.10f' % self.weightAmountHoles
        output += '\n -wRoughness      : %0.10f' % self.weightRoughness
        return output + '\n'


    def initialGenome( self ):
        self.weightRowsCleared    = np.random.random( ) - 0.5
        self.weightMaxHeight      = np.random.random( ) - 0.5
        self.weightSumHeight      = np.random.random( ) - 0.5
        self.weightRelativeHeight = np.random.random( ) - 0.5
        self.weightAmountHoles    = np.random.random( ) - 0.5
        self.weightRoughness      = np.random.random( ) - 0.5

    def cross( self, mum, dad ):
        self.weightRowsCleared    = choice( [ mum.weightRowsCleared   , dad.weightRowsCleared    ] )
        self.weightMaxHeight      = choice( [ mum.weightMaxHeight     , dad.weightMaxHeight      ] )
        self.weightSumHeight      = choice( [ mum.weightSumHeight     , dad.weightSumHeight      ] )
        self.weightRelativeHeight = choice( [ mum.weightRelativeHeight, dad.weightRelativeHeight ] )
        self.weightAmountHoles    = choice( [ mum.weightAmountHoles   , dad.weightAmountHoles    ] )
        self.weightRoughness      = choice( [ mum.weightRoughness     , dad.weightRoughness      ] )
        self.mum                  = mum.identifier
        self.dad                  = dad.identifier

    def mutate( self ):
        if np.random.random( ) < self.mutationRate:
            self.weightRowsCleared    = self.weightRowsCleared   + self.mutationStep * ( 2 * np.random.random( ) - 1 )
        if np.random.random( ) < self.mutationRate:
            self.weightMaxHeight      = self.weightMaxHeight     + self.mutationStep * ( 2 * np.random.random( ) - 1 )
        if np.random.random( ) < self.mutationRate:
            self.weightSumHeight      = self.weightSumHeight     + self.mutationStep * ( 2 * np.random.random( ) - 1 )
        if np.random.random( ) < self.mutationRate:
            self.weightRelativeHeight = self.weightRelativeHeight+ self.mutationStep * ( 2 * np.random.random( ) - 1 )
        if np.random.random( ) < self.mutationRate:
            self.weightAmountHoles    = self.weightAmountHoles   + self.mutationStep * ( 2 * np.random.random( ) - 1 )
        if np.random.random( ) < self.mutationRate:
            self.weightRoughness      = self.weightRoughness     + self.mutationStep * ( 2 * np.random.random( ) - 1 )

    __repr__ = __str__
