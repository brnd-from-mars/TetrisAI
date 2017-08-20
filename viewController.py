# viewController.py


import pygame as gui
import numpy as np
import os


class ViewController( object ):

    rd = ( 249,  35,  56 )
    pk = ( 201, 115, 255 )
    bl = (  28, 118, 188 )
    yw = ( 254, 227,  86 )
    gn = (  83, 213,   4 )
    cy = (  54, 224, 255 )
    og = ( 248, 147,  29 )
    dk = (  39,  40,  33 )
    lg = ( 112, 108,  90 )
    colors = [ dk, rd, pk, bl, yw, gn, cy, og ]

    def __init__( self, grid, time, score, ai, grapher ):

        try:
            os.environ['SDL_VIDEO_WINDOW_POS'] = '10,50'
        except:
            pass
        self.grid = grid
        self.time = time
        self.score = score
        self.ai = ai
        self.grapher = grapher
        self.abort = False
        self.update = True
        self.infoMode = 0
        self.genomeScreen = [ 0, -1 ]
        self.aiState = False
        #gui.init( )
        self.screen = gui.display.set_mode( ( 820,720 ) )
        self.fontBold = gui.font.Font( 'font/texgyrecursor-bold.otf', 60 )
        self.fontRegular = gui.font.Font( 'font/texgyrecursor-regular.otf', 30 )
        self.fontSmall = gui.font.Font( 'font/texgyrecursor-regular.otf', 15 )
        self.updateStatic( True )

    def updateStatic( self, render=False ):
        if not render:
            self.screen.blit( self.static, ( 0, 0 ) )
            return
        static = gui.Surface( ( 840, 720 ) )
        static.set_colorkey( ( 0, 0, 0 ) )
        # background
        static.fill( self.dk )
        # draw seperator
        gui.draw.line(static, self.lg, ( 420, 0 ), ( 420, 720 ), 2 )
        gui.draw.line(static, self.lg, ( 420, 360 ), ( 840, 360 ), 2 )
        # draw grid lines
        for i in range( 10 ):
            gui.draw.line(static, self.lg, ( 30*i+60, 60 ), ( 30*i+60, 660 ) )
            gui.draw.line(static, self.lg, ( 60, 30*i+60 ), ( 360, 30*i+60 ), 1+2*(i==4) )
            gui.draw.line(static, self.lg, ( 60, 30*i+390 ), ( 360, 30*i+390 ) )
        gui.draw.line(static, self.lg, ( 360, 60 ), ( 360, 660 ) )
        gui.draw.line(static, self.lg, ( 60, 360 ), ( 360, 360 ) )
        # draw tile preview
        for i in range( 5 ):
            gui.draw.line(static, self.lg, ( 480, 30*i+180), ( 600, 30*i+180) )
            gui.draw.line(static, self.lg, ( 30*i+480, 180), ( 30*i+480, 300) )
        # draw headline
        label = self.fontBold.render( 'TetrisAI', 2, self.lg )
        size = self.fontBold.size( 'TetrisAI' )[ 0 ]
        static.blit( label, ( 615-size/2, 30 ) )
        # draw buttons
        gui.draw.rect( static, self.lg, gui.Rect( 480, 630, 101, 30 ), 1 )
        gui.draw.rect( static, self.lg, gui.Rect( 580, 630, 101, 30 ), 1 )
        gui.draw.rect( static, self.lg, gui.Rect( 680, 630, 101, 30 ), 1 )
        label = self.fontSmall.render( 'General', 2, self.lg )
        static.blit( label, ( 485, 630 ) )
        label = self.fontSmall.render( 'Genomes', 2, self.lg )
        static.blit( label, ( 585, 630 ) )
        label = self.fontSmall.render( 'Graph', 2, self.lg )
        static.blit( label, ( 685, 630 ) )
        # apply
        self.static = static

    def setUpdate( self, update ):
        self.update = update

    def setTile( self, cTile, nTile ):
        self.cTile = cTile
        self.nTile = nTile

    def updateGrid( self ):
        grid = self.grid.grid  + self.cTile.render( )
        for x in range( 10 ):
            for y in range( 20 ):
                color = self.colors[ grid[ x, y ] ]
                gui.draw.rect( self.screen, color, gui.Rect( 30*x+65, 30*y+65, 21, 21 ), 0 )

    def updateGameScreen( self ):
        color = self.colors[ self.nTile.identifier ]
        preview = self.nTile.renderPreview( )
        for x in range( 4 ):
            for y in range( 4 ):
                if preview[ x, y ] != 0:
                    gui.draw.rect( self.screen, color, gui.Rect( 30*x+485, 30*y+185, 21, 21 ), 0 )

        label = self.fontRegular.render( str( self.score.getScore( ) ), 2, self.lg )
        size = self.fontRegular.size( str( self.score.getScore( ) ) )[ 0 ]
        self.screen.blit( label, ( 780-size, 180 ) )

        label = self.fontRegular.render( str( self.score.getHighscore( ) ), 2, self.lg )
        size = self.fontRegular.size( str( self.score.getHighscore( ) ) )[ 0 ]
        self.screen.blit( label, ( 780-size, 240 ) )

    def updateGeneralScreen( self ):
        gui.draw.rect(self.screen, self.lg, gui.rect.Rect( 480, 420, 300, 10 ), 1 )
        self.progress = self.time.getIntvProgress( )
        gui.draw.rect( self.screen, self.lg, gui.rect.Rect( 480, 420, min( 300, 300*self.progress ), 10 ) )

        label = self.fontRegular.render( 'Speed', 2, self.lg )
        self.screen.blit( label, ( 480, 450 ) )
        label = self.fontRegular.render( str( self.time.getSpeed( ) )+'x', 2, self.lg )
        size = self.fontRegular.size( str( self.time.getSpeed( ) )+'x' )[ 0 ]
        self.screen.blit( label, ( 780-size, 450 ) )

        label = self.fontRegular.render( 'Generation', 2, self.lg )
        self.screen.blit( label, ( 480, 480 ) )
        label = self.fontRegular.render( str( self.ai.currentGeneration ), 2, self.lg )
        size = self.fontRegular.size( str( self.ai.currentGeneration ) )[ 0 ]
        self.screen.blit( label, ( 780-size, 480 ) )

        label = self.fontRegular.render( 'Genom', 2, self.lg )
        self.screen.blit( label, ( 480, 510 ) )
        label = self.fontRegular.render( str( self.ai.currentGenome ), 2, self.lg )
        size = self.fontRegular.size( str( self.ai.currentGenome ) )[ 0 ]
        self.screen.blit( label, ( 780-size, 510 ) )

    def updateGenomeScreen( self ):
        gui.draw.rect( self.screen, self.lg, gui.Rect( 630, 405, 39, 30 ), 1 )
        gui.draw.rect( self.screen, self.lg, gui.Rect( 668, 405, 39, 30 ), 1 )
        gui.draw.rect( self.screen, self.lg, gui.Rect( 706, 405, 39, 30 ), 1 )
        gui.draw.rect( self.screen, self.lg, gui.Rect( 744, 405, 39, 30 ), 1 )

        label = self.fontSmall.render( str( self.genomeScreen[ 0 ] ) + '/' + str( len( self.ai.population.generations )-1 ) + ': ' + str( self.genomeScreen[ 1 ] ), 2, self.lg )
        self.screen.blit( label, ( 480, 400 ) )

        if self.genomeScreen[ 1 ] == -1:
            for i in range( 10 ):
                label = self.fontSmall.render( '%d:' % i, 2, self.lg )
                self.screen.blit( label, ( 445, 450+15*i ) )
            for i in range( 40 ):
                score = self.ai.population.generations[ self.genomeScreen[ 0 ] ].genomes[ i ].score
                label = self.fontSmall.render( str( score ), 2, self.lg )
                self.screen.blit( label, ( 480+75*int(i/10), 450+15*(i%10) ) )
        else:
            genome = str( self.ai.population.generations[ self.genomeScreen[ 0 ] ].genomes[ self.genomeScreen[ 1 ] ] ).split( '\n' )
            i = 0
            for line in genome:
                if line != '':
                    label = self.fontSmall.render( str( line ), 2, self.lg )
                    self.screen.blit( label, ( 480, 450+15*i ) )
                    i += 1

    def updateGraphScreen( self ):
        self.screen.blit( self.grapher.lastGraph, (480, 400) )


    def eventCheck( self ):
        for event in gui.event.get( ):
            if event.type == gui.QUIT:
                self.abort = True
            if event.type == gui.KEYDOWN:
                if event.key == gui.K_ESCAPE:
                    gui.event.post( gui.event.Event( gui.QUIT ) )
                if event.key == gui.K_LEFT:
                    self.cTile.decX( )
                if event.key == gui.K_RIGHT:
                    self.cTile.incX( )
                if event.key == gui.K_DOWN:
                    self.cTile.incY( )
                if event.key == gui.K_COMMA:
                    self.cTile.rotACW( )
                if event.key == gui.K_PERIOD:
                    self.cTile.rotCW( )
                if event.key == gui.K_RETURN:
                    self.cTile.drop( )
                if event.key == gui.K_p:
                    self.time.incSpeed( )
                if event.key == gui.K_o:
                    self.time.decSpeed( )
                if event.key == gui.K_a:
                    self.aiState = not self.aiState
            if event.type == gui.MOUSEBUTTONUP:
                if event.button == 1:
                    if gui.Rect( 480, 630, 101, 30 ).collidepoint( event.pos ):
                        self.infoMode = 0
                    if gui.Rect( 580, 630, 101, 30 ).collidepoint( event.pos ):
                        self.infoMode = 1
                    if gui.Rect( 680, 630, 101, 30 ).collidepoint( event.pos ):
                        self.infoMode = 2
                    if self.infoMode == 1:
                        if gui.Rect( 630, 405, 39, 30 ).collidepoint( event.pos ):
                            self.genomeScreen[ 0 ] = max( 0, self.genomeScreen[ 0 ]-1 )
                        if gui.Rect( 668, 405, 39, 30 ).collidepoint( event.pos ):
                            self.genomeScreen[ 0 ] = min( len( self.ai.population.generations )-1, self.genomeScreen[ 0 ]+1 )
                        if gui.Rect( 706, 405, 39, 30 ).collidepoint( event.pos ):
                            self.genomeScreen[ 1 ] = max( -1, self.genomeScreen[ 1 ]-1 )
                        if gui.Rect( 744, 405, 39, 30 ).collidepoint( event.pos ):
                            self.genomeScreen[ 1 ] = min( 39, self.genomeScreen[ 1 ]+1 )

    def updateEverything( self ):
        self.eventCheck( )
        if not self.update:
            return
        self.updateStatic( )
        self.updateGrid( )
        self.updateGameScreen( )
        if self.infoMode == 0:
            self.updateGeneralScreen( )
        if self.infoMode == 1:
            self.updateGenomeScreen( )
        if self.infoMode == 2:
            self.updateGraphScreen( )
        gui.display.flip( )
