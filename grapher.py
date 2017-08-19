# grapher.py


import pygame as gui
import numpy as np


class Grapher( object ):

    def __init__( self, score ):
        gui.init( )
        self.score = score
        self.genScores = [ ]
        self.highScore = 1
        self.lastGraph = gui.Surface( ( 300, 200 ) )
        self.lastGraph.set_colorkey( ( 0, 0, 0 ) )

    def appendDataSet( self, generationScores ):
        scores = np.sort( np.array( generationScores ) )
        self.genScores.append( scores )
        self.highScore = self.score.highest
        self.drawGraph( )

    def drawGraph( self ):
        graph = gui.Surface( ( 300, 200 ) )
        graph.set_colorkey( ( 0, 0, 0 ) )
        gens = len( self.genScores )
        for genome in range( 40 ):
            pointlist = [ ( 0, 200 ) ]
            for generation in range( gens ):
                x = int( 300 * ( generation+1 ) / gens )
                y = 200 - int( 200 * self.genScores[ generation ][ genome ] / self.highScore  )
                pointlist.append( ( x, y ) )
            if genome in [ 0, 19, 39 ]:
                gui.draw.lines( graph, ( 0, 0, 255 ), False, pointlist, 2 )
            else:
                gui.draw.lines( graph, ( 112, 108, 90 ), False, pointlist, 1 )
        pointlist = [ ( 0, 200 ) ]
        for generation in range( gens ):
            x = int( 300 * ( generation+1 ) / gens )
            y = 200 - int( 200 * np.average( self.genScores[ generation ] ) / self.highScore  )
            pointlist.append( ( x, y ) )
        gui.draw.lines( graph, ( 255, 0,  0 ), False, pointlist, 2 )

        self.lastGraph = graph
