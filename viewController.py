# viewController.py


import pygame as gui
import numpy as np
import gridController
import tileController
import timeController


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

    def __init__( self, grid, time ):

        self.grid = grid
        self.time = time
        self.abort = False
        gui.init( )
        self.screen = gui.display.set_mode( ( 800,700 ) )
        self.updateStatic( True )

    def updateStatic( self, render=False ):
        if not render:
            self.screen.blit( self.static, ( 0, 0 ) )
            return
        static = gui.Surface( ( 800, 700 ) )
        static.set_colorkey( ( 0, 0, 0 ) )
        # background
        static.fill( self.dk )
        # draw grid lines
        for i in range( 10 ):
            gui.draw.line(static, self.lg, ( 30*i+50, 50 ), ( 30*i+50, 650 ) )
            gui.draw.line(static, self.lg, ( 50, 30*i+50 ), ( 350, 30*i+50 ), 1+2*(i==4) )
            gui.draw.line(static, self.lg, ( 50, 30*i+380 ), ( 350, 30*i+380 ) )
        gui.draw.line(static, self.lg, ( 350, 50 ), ( 350, 650 ) )
        gui.draw.line(static, self.lg, ( 50, 350 ), ( 350, 350 ) )
        # draw seperator
        gui.draw.line(static, self.lg, ( 400, 0 ), ( 400, 700 ), 2 )
        # draw event time bar
        gui.draw.rect(static, self.lg, gui.rect.Rect( 450, 50, 300, 30 ), 1 )
        # apply
        self.static = static


    def setTile( self, tile ):
        self.tile = tile

    def updateGrid( self ):
        grid = self.grid.grid  + self.tile.render( )
        for x in range( 10 ):
            for y in range( 20 ):
                color = self.colors[ grid[ x, y ] ]
                gui.draw.rect( self.screen, color, gui.Rect( 30*x+55, 30*y+55, 21, 21 ), 0 )

    def updateTime( self ):
        self.progress = self.time.getIntvProgress( )
        gui.draw.rect( self.screen, self.lg, gui.rect.Rect( 450, 50, 300*self.progress, 30 ) )

    def eventCheck( self ):
        for event in gui.event.get( ):
            if event.type == gui.QUIT:
                self.abort = True
            if event.type == gui.KEYDOWN:
                if event.key == gui.K_ESCAPE:
                    gui.event.post( gui.event.Event( gui.QUIT ) )
                if event.key == gui.K_LEFT:
                    self.tile.decX( )
                if event.key == gui.K_RIGHT:
                    self.tile.incX( )
                if event.key == gui.K_DOWN:
                    self.tile.incY( )
                if event.key == gui.K_COMMA:
                    self.tile.rotACW( )
                if event.key == gui.K_PERIOD:
                    self.tile.rotCW( )



    def update( self ):
        self.eventCheck( )
        self.updateStatic( )
        self.updateGrid( )
        self.updateTime( )
        gui.display.flip( )
