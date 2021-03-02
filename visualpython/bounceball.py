#!/usr/bin/env python3

from __future__ import division
from vpython import *
import vpython as vp
import numpy as np

UNIT = 1.0
SCALE_DN = 0.30
SCALE_UP = 1.30

class Universe:
    def __init__(self):
        
        self.viewScene()
        self.cartAxis()

    def viewScene(self):
        """ Canvas Scene """
        scene = vp.canvas(
                title = "World Universe",
                fullscreen = True,
                x = 0, y = 0,
                width = 1600, height = 900,
                center = vector(0, 0, 0),
                background = color.black,   # Color to fill canvas
                ambient = color.gray(0.2),  # Color of nondirectional/ambient light
                resizable = True,
                visible = True,
        )

    def cartAxis(self):
        """ Cartesian Coordinates """
        xaxis = cylinder(pos=vector(0, 0, 0), axis=vector(1,0,0), radius=0.01, length=UNIT)
        yaxis = cylinder(pos=vector(0, 0, 0), axis=vector(0,1,0), radius=0.01, length=UNIT)
        zaxis = cylinder(pos=vector(0, 0, 0), axis=vector(0,0,1), radius=0.01, length=UNIT)
        xlabel = label(text="x-axis", pos=xaxis.axis, font="sans", space=xaxis.radius)
        ylabel = label(text="y-axis", pos=yaxis.axis, font="sans", space=yaxis.radius)
        zlabel = label(text="z-axis", pos=zaxis.axis, font="sans", space=zaxis.radius)

        
class Assets(Universe):
    def __init__(self):
        Universe.__init__(self)
        
        self.ball = sphere(
                    pos=vector(UNIT/10, UNIT/10, UNIT/10),
                    color=color.red,
                    radius=0.1
                )
        self.floor = box(
                    pos=vector(0, 0, 0), color=color.green,
                    size=vector(2*UNIT, 0.01, 2*UNIT)
                )

class InitialConditions(Assets):
    def __init__(self):
        """ Setting up initial conditions """
        Assets.__init__(self)

        self.ball.velocity = vector(0, 5, 0)
        self.ball.mass = 0.25
        self.ball.momentum = self.ball.mass * self.ball.velocity
        g = vector(0, -9.8, 0)
        self.dt = 0.001
        self.t = 0
        self.C = 0.75
        self.rho = 2.25
        self.area = 2 * np.pi * self.ball.radius**2
        self.fg = (g * self.ball.mass)

class Events(InitialConditions):
    def __init__(self):
        """ Physics Events Simulation """
        InitialConditions.__init__(self)

        trail = curve(color=color.white)    # Trail
        posgraph = gcurve(color=color.cyan) # Graph
        pvector = arrow(pos=self.ball.pos, axis=self.ball.momentum)   # Adding arrow to represent vectors


        while (self.t < 10):
            rate(300)
            trail.append(pos=self.ball.pos)
            posgraph.plot(pos=(self.t, self.ball.pos.y))
            pvector.pos = self.ball.pos
            pvector.axis = self.ball.momentum * SCALE_DN
    
            # Air Resistance = -0.5 * rho * C * A * v^2 * v^hat
            self.fnet = self.fg - ( 0.5 * self.C * self.rho * self.area * mag(self.ball.momentum/self.ball.mass)**2 * 
                    self.ball.momentum/mag(self.ball.momentum) )

            self.ball.pos = self.ball.pos + ( (self.ball.momentum/self.ball.mass) * self.dt )
            self.ball.momentum = self.ball.momentum + (self.fnet * self.dt)
            self.t = self.t + self.dt

            # Bouncing on the floor
            if ( self.ball.pos.y < (self.floor.pos.y + self.ball.radius) ):
                self.ball.momentum.y= -self.ball.momentum.y


Events()
