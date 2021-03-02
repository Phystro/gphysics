#!/usr/bin/env python3

import vpython as vp
import numpy as np
from vpython import *
from time import sleep

AMP = 10.0
RADIUS = 0.2

class Universe:
    def __init__(self):

        self.viewScene()
    

    def viewScene(self):
        """ Canvas Scene """
        scene = vp.canvas(
                    title = "Oscillations",
                    x = 0, y = 0,
                    width = 1600, height = 900,
                )


class Assets(Universe):
    def __init__(self):
        """Physical objects"""
        Universe.__init__(self)

        self.point0c = sphere( pos = vector(0, 0, 0), color = color.red, radius = RADIUS )

        self.point1l = sphere( pos = vector(-1, 0, 0), color = color.red, radius = RADIUS )
        self.point2l = sphere( pos = vector(-2, 0, 0), color = color.red, radius = RADIUS )
        self.point3l = sphere( pos = vector(-3, 0, 0), color = color.red, radius = RADIUS )
        self.point4l = sphere( pos = vector(-4, 0, 0), color = color.red, radius = RADIUS )
        self.point5l = sphere( pos = vector(-5, 0, 0), color = color.red, radius = RADIUS )
        self.point6l = sphere( pos = vector(-6, 0, 0), color = color.orange, radius = RADIUS )
        self.point7l = sphere( pos = vector(-7, 0, 0), color = color.orange, radius = RADIUS )
        self.point8l = sphere( pos = vector(-8, 0, 0), color = color.orange, radius = RADIUS )
        self.point9l = sphere( pos = vector(-9, 0, 0), color = color.orange, radius = RADIUS )
        self.point10l = sphere( pos = vector(-10, 0, 0), color = color.orange, radius = RADIUS )
        self.point11l = sphere( pos = vector(-11, 0, 0), color = color.yellow, radius = RADIUS )
        self.point12l = sphere( pos = vector(-12, 0, 0), color = color.yellow, radius = RADIUS )
        self.point13l = sphere( pos = vector(-13, 0, 0), color = color.yellow, radius = RADIUS )
        self.point14l = sphere( pos = vector(-14, 0, 0), color = color.yellow, radius = RADIUS )
        self.point15l = sphere( pos = vector(-15, 0, 0), color = color.yellow, radius = RADIUS )
        self.point16l = sphere( pos = vector(-16, 0, 0), color = color.green, radius = RADIUS )
        self.point17l = sphere( pos = vector(-17, 0, 0), color = color.green, radius = RADIUS )
        self.point18l = sphere( pos = vector(-18, 0, 0), color = color.green, radius = RADIUS )
        self.point19l = sphere( pos = vector(-19, 0, 0), color = color.green, radius = RADIUS )
        self.point20l = sphere( pos = vector(-20, 0, 0), color = color.green, radius = RADIUS )
        self.point21l = sphere( pos = vector(-21, 0, 0), color = color.cyan, radius = RADIUS )
        self.point22l = sphere( pos = vector(-22, 0, 0), color = color.cyan, radius = RADIUS )
        self.point23l = sphere( pos = vector(-23, 0, 0), color = color.cyan, radius = RADIUS )
        self.point24l = sphere( pos = vector(-24, 0, 0), color = color.cyan, radius = RADIUS )
        self.point25l = sphere( pos = vector(-25, 0, 0), color = color.cyan, radius = RADIUS )
        self.point26l = sphere( pos = vector(-26, 0, 0), color = color.blue, radius = RADIUS )
        self.point27l = sphere( pos = vector(-27, 0, 0), color = color.blue, radius = RADIUS )
        self.point28l = sphere( pos = vector(-28, 0, 0), color = color.blue, radius = RADIUS )
        self.point29l = sphere( pos = vector(-29, 0, 0), color = color.blue, radius = RADIUS )
        self.point30l = sphere( pos = vector(-30, 0, 0), color = color.blue, radius = RADIUS )
        self.point31l = sphere( pos = vector(-31, 0, 0), color = color.purple, radius = RADIUS )
        self.point32l = sphere( pos = vector(-32, 0, 0), color = color.purple, radius = RADIUS )
        self.point33l = sphere( pos = vector(-33, 0, 0), color = color.purple, radius = RADIUS )
        self.point34l = sphere( pos = vector(-34, 0, 0), color = color.purple, radius = RADIUS )
        self.point35l = sphere( pos = vector(-35, 0, 0), color = color.purple, radius = RADIUS )



        self.point1r = sphere( pos = vector(1, 0, 0), color = color.red, radius = RADIUS )
        self.point2r = sphere( pos = vector(2, 0, 0), color = color.red, radius = RADIUS )
        self.point3r = sphere( pos = vector(3, 0, 0), color = color.red, radius = RADIUS )
        self.point4r = sphere( pos = vector(4, 0, 0), color = color.red, radius = RADIUS )
        self.point5r = sphere( pos = vector(5, 0, 0), color = color.red, radius = RADIUS )
        self.point6r = sphere( pos = vector(6, 0, 0), color = color.orange, radius = RADIUS )
        self.point7r = sphere( pos = vector(7, 0, 0), color = color.orange, radius = RADIUS )
        self.point8r = sphere( pos = vector(8, 0, 0), color = color.orange, radius = RADIUS )
        self.point9r = sphere( pos = vector(9, 0, 0), color = color.orange, radius = RADIUS )
        self.point10r = sphere( pos = vector(10, 0, 0), color = color.orange, radius = RADIUS )
        self.point11r = sphere( pos = vector(11, 0, 0), color = color.yellow, radius = RADIUS )
        self.point12r = sphere( pos = vector(12, 0, 0), color = color.yellow, radius = RADIUS )
        self.point13r = sphere( pos = vector(13, 0, 0), color = color.yellow, radius = RADIUS )
        self.point14r = sphere( pos = vector(14, 0, 0), color = color.yellow, radius = RADIUS )
        self.point15r = sphere( pos = vector(15, 0, 0), color = color.yellow, radius = RADIUS )
        self.point16r = sphere( pos = vector(16, 0, 0), color = color.green, radius = RADIUS )
        self.point17r = sphere( pos = vector(17, 0, 0), color = color.green, radius = RADIUS )
        self.point18r = sphere( pos = vector(18, 0, 0), color = color.green, radius = RADIUS )
        self.point19r = sphere( pos = vector(19, 0, 0), color = color.green, radius = RADIUS )
        self.point20r = sphere( pos = vector(20, 0, 0), color = color.green, radius = RADIUS )
        self.point21r = sphere( pos = vector(21, 0, 0), color = color.cyan, radius = RADIUS )
        self.point22r = sphere( pos = vector(22, 0, 0), color = color.cyan, radius = RADIUS )
        self.point23r = sphere( pos = vector(23, 0, 0), color = color.cyan, radius = RADIUS )
        self.point24r = sphere( pos = vector(24, 0, 0), color = color.cyan, radius = RADIUS )
        self.point25r = sphere( pos = vector(25, 0, 0), color = color.cyan, radius = RADIUS )
        self.point26r = sphere( pos = vector(26, 0, 0), color = color.blue, radius = RADIUS )
        self.point27r = sphere( pos = vector(27, 0, 0), color = color.blue, radius = RADIUS )
        self.point28r = sphere( pos = vector(28, 0, 0), color = color.blue, radius = RADIUS )
        self.point29r = sphere( pos = vector(29, 0, 0), color = color.blue, radius = RADIUS )
        self.point30r = sphere( pos = vector(30, 0, 0), color = color.blue, radius = RADIUS )
        self.point31r = sphere( pos = vector(31, 0, 0), color = color.purple, radius = RADIUS )
        self.point32r = sphere( pos = vector(32, 0, 0), color = color.purple, radius = RADIUS )
        self.point33r = sphere( pos = vector(33, 0, 0), color = color.purple, radius = RADIUS )
        self.point34r = sphere( pos = vector(34, 0, 0), color = color.purple, radius = RADIUS )
        self.point35r = sphere( pos = vector(35, 0, 0), color = color.purple, radius = RADIUS )


class InitialConditions(Assets):
    def __init__(self):
        """ Setting up the initial conditions"""
        Assets.__init__(self)

        self.t = 0
        self.dt = 0.001


class Events(InitialConditions):
    def __init__(self):
        """Physics events simulation"""
        InitialConditions.__init__(self)

        sleep(3)

        while (True):
            rate(100)

            # calculate y position
            self.point0c.pos.y = AMP * np.sin( self.point0c.pos.x * self.t );

            self.point1l.pos.y = AMP * np.sin( self.point1l.pos.x * self.t );
            self.point2l.pos.y = AMP * np.sin( self.point2l.pos.x * self.t );
            self.point3l.pos.y = AMP * np.sin( self.point3l.pos.x * self.t );
            self.point4l.pos.y = AMP * np.sin( self.point4l.pos.x * self.t );
            self.point5l.pos.y = AMP * np.sin( self.point5l.pos.x * self.t );
            self.point6l.pos.y = AMP * np.sin( self.point6l.pos.x * self.t );
            self.point7l.pos.y = AMP * np.sin( self.point7l.pos.x * self.t );
            self.point8l.pos.y = AMP * np.sin( self.point8l.pos.x * self.t );
            self.point9l.pos.y = AMP * np.sin( self.point9l.pos.x * self.t );
            self.point10l.pos.y = AMP * np.sin( self.point10l.pos.x * self.t );
            self.point11l.pos.y = AMP * np.sin( self.point11l.pos.x * self.t );
            self.point12l.pos.y = AMP * np.sin( self.point12l.pos.x * self.t );
            self.point13l.pos.y = AMP * np.sin( self.point13l.pos.x * self.t );
            self.point14l.pos.y = AMP * np.sin( self.point14l.pos.x * self.t );
            self.point15l.pos.y = AMP * np.sin( self.point15l.pos.x * self.t );
            self.point16l.pos.y = AMP * np.sin( self.point16l.pos.x * self.t );
            self.point17l.pos.y = AMP * np.sin( self.point17l.pos.x * self.t );
            self.point18l.pos.y = AMP * np.sin( self.point18l.pos.x * self.t );
            self.point19l.pos.y = AMP * np.sin( self.point19l.pos.x * self.t );
            self.point20l.pos.y = AMP * np.sin( self.point20l.pos.x * self.t );
            self.point21l.pos.y = AMP * np.sin( self.point21l.pos.x * self.t );
            self.point22l.pos.y = AMP * np.sin( self.point22l.pos.x * self.t );
            self.point23l.pos.y = AMP * np.sin( self.point23l.pos.x * self.t );
            self.point24l.pos.y = AMP * np.sin( self.point24l.pos.x * self.t );
            self.point25l.pos.y = AMP * np.sin( self.point25l.pos.x * self.t );
            self.point26l.pos.y = AMP * np.sin( self.point26l.pos.x * self.t );
            self.point27l.pos.y = AMP * np.sin( self.point27l.pos.x * self.t );
            self.point28l.pos.y = AMP * np.sin( self.point28l.pos.x * self.t );
            self.point29l.pos.y = AMP * np.sin( self.point29l.pos.x * self.t );
            self.point30l.pos.y = AMP * np.sin( self.point30l.pos.x * self.t );
            self.point31l.pos.y = AMP * np.sin( self.point31l.pos.x * self.t );
            self.point32l.pos.y = AMP * np.sin( self.point32l.pos.x * self.t );
            self.point33l.pos.y = AMP * np.sin( self.point33l.pos.x * self.t );
            self.point34l.pos.y = AMP * np.sin( self.point34l.pos.x * self.t );
            self.point35l.pos.y = AMP * np.sin( self.point35l.pos.x * self.t );

            self.point1r.pos.y = AMP * np.sin( self.point1r.pos.x * self.t );
            self.point2r.pos.y = AMP * np.sin( self.point2r.pos.x * self.t );
            self.point3r.pos.y = AMP * np.sin( self.point3r.pos.x * self.t );
            self.point4r.pos.y = AMP * np.sin( self.point4r.pos.x * self.t );
            self.point5r.pos.y = AMP * np.sin( self.point5r.pos.x * self.t );
            self.point6r.pos.y = AMP * np.sin( self.point6r.pos.x * self.t );
            self.point7r.pos.y = AMP * np.sin( self.point7r.pos.x * self.t );
            self.point8r.pos.y = AMP * np.sin( self.point8r.pos.x * self.t );
            self.point9r.pos.y = AMP * np.sin( self.point9r.pos.x * self.t );
            self.point10r.pos.y = AMP * np.sin( self.point10r.pos.x * self.t );
            self.point11r.pos.y = AMP * np.sin( self.point11r.pos.x * self.t );
            self.point12r.pos.y = AMP * np.sin( self.point12r.pos.x * self.t );
            self.point13r.pos.y = AMP * np.sin( self.point13r.pos.x * self.t );
            self.point14r.pos.y = AMP * np.sin( self.point14r.pos.x * self.t );
            self.point15r.pos.y = AMP * np.sin( self.point15r.pos.x * self.t );
            self.point16r.pos.y = AMP * np.sin( self.point16r.pos.x * self.t );
            self.point17r.pos.y = AMP * np.sin( self.point17r.pos.x * self.t );
            self.point18r.pos.y = AMP * np.sin( self.point18r.pos.x * self.t );
            self.point19r.pos.y = AMP * np.sin( self.point19r.pos.x * self.t );
            self.point20r.pos.y = AMP * np.sin( self.point20r.pos.x * self.t );
            self.point21r.pos.y = AMP * np.sin( self.point21r.pos.x * self.t );
            self.point22r.pos.y = AMP * np.sin( self.point22r.pos.x * self.t );
            self.point23r.pos.y = AMP * np.sin( self.point23r.pos.x * self.t );
            self.point24r.pos.y = AMP * np.sin( self.point24r.pos.x * self.t );
            self.point25r.pos.y = AMP * np.sin( self.point25r.pos.x * self.t );
            self.point26r.pos.y = AMP * np.sin( self.point26r.pos.x * self.t );
            self.point27r.pos.y = AMP * np.sin( self.point27r.pos.x * self.t );
            self.point28r.pos.y = AMP * np.sin( self.point28r.pos.x * self.t );
            self.point29r.pos.y = AMP * np.sin( self.point29r.pos.x * self.t );
            self.point30r.pos.y = AMP * np.sin( self.point30r.pos.x * self.t );
            self.point31r.pos.y = AMP * np.sin( self.point31r.pos.x * self.t );
            self.point32r.pos.y = AMP * np.sin( self.point32r.pos.x * self.t );
            self.point33r.pos.y = AMP * np.sin( self.point33r.pos.x * self.t );
            self.point34r.pos.y = AMP * np.sin( self.point34r.pos.x * self.t );
            self.point35r.pos.y = AMP * np.sin( self.point35r.pos.x * self.t );

            self.t += self.dt


Events()

