# viewController.py


import pygame as gui
import numpy as np


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

    def __init__( self, grid, time, score ):

        self.grid = grid
        self.time = time
        self.score = score
        self.abort = False
        gui.init( )
        self.screen = gui.display.set_mode( ( 820,720 ) )
        self.fontBold = gui.font.Font( 'font/texgyrecursor-bold.otf', 60 )
        self.fontRegular = gui.font.Font( 'font/texgyrecursor-regular.otf', 30 )
        self.fontSmall = gui.font.Font( 'font/texgyrecursor-regular.otf', 20 )
        self.updateStatic( True )

    def updateStatic( self, render=False ):
        if not render:
            self.screen.blit( self.static, ( 0, 0 ) )
            return
        static = gui.Surface( ( 820, 720 ) )
        static.set_colorkey( ( 0, 0, 0 ) )
        # background
        static.fill( self.dk )
        # draw seperator
        gui.draw.line(static, self.lg, ( 410, 0 ), ( 410, 720 ), 2 )
        gui.draw.line(static, self.lg, ( 410, 360 ), ( 820, 360 ), 2 )
        # draw grid lines
        for i in range( 10 ):
            gui.draw.line(static, self.lg, ( 30*i+60, 60 ), ( 30*i+60, 660 ) )
            gui.draw.line(static, self.lg, ( 60, 30*i+60 ), ( 360, 30*i+60 ), 1+2*(i==4) )
            gui.draw.line(static, self.lg, ( 60, 30*i+390 ), ( 360, 30*i+390 ) )
        gui.draw.line(static, self.lg, ( 360, 60 ), ( 360, 660 ) )
        gui.draw.line(static, self.lg, ( 60, 360 ), ( 360, 360 ) )
        # draw tile preview
        for i in range( 5 ):
            gui.draw.line(static, self.lg, ( 470, 30*i+180), ( 590, 30*i+180) )
            gui.draw.line(static, self.lg, ( 30*i+470, 180), ( 30*i+470, 300) )
        # draw event time bar
        gui.draw.rect(static, self.lg, gui.rect.Rect( 470, 420, 290, 10 ), 1 )
        # draw headline
        header = self.fontBold.render( 'TetrisAI', 2, self.lg )
        size = self.fontBold.size( 'TetrisAI' )[ 0 ]
        static.blit( header, ( 615-size/2, 30 ) )
        # apply
        self.static = static


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
                    gui.draw.rect( self.screen, color, gui.Rect( 30*x+475, 30*y+185, 21, 21 ), 0 )
        score = self.fontRegular.render( str( self.score.getScore( ) ), 2, self.lg )
        size = self.fontRegular.size( str( self.score.getScore( ) ) )[ 0 ]
        self.screen.blit( score, ( 760-size, 180 ) )
        score = self.fontSmall.render( str( self.score.getHighscore( ) ), 2, self.lg )
        size = self.fontSmall.size( str( self.score.getHighscore( ) ) )[ 0 ]
        self.screen.blit( score, ( 760-size, 210 ) )


    def updateDebugScreen( self ):
        self.progress = self.time.getIntvProgress( )
        gui.draw.rect( self.screen, self.lg, gui.rect.Rect( 470, 420, 290*self.progress, 10 ) )

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
                    self.cTile.drop()

    def update( self ):
        self.eventCheck( )
        self.updateStatic( )
        self.updateGrid( )
        self.updateGameScreen( )
        self.updateDebugScreen( )
        gui.display.flip( )
