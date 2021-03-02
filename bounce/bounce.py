#!/usr/bin/env python3

from __future__ import division
from vpython import *
import vpython as vp
import numpy as np
from time import sleep

UNIT = 1.0
NORM = 1.0
SCALE_UP = 1.300
SCALE_DW = 0.300

class Universe:
    def __init__(self):

        self.viewScene()
        self.cartAxis()

    def viewScene(self):
        """ Canvas Scene """
        scene = vp.canvas(
                    title = "Bouncing Ball",
                    x = 0, y = 0,
                    width = 1600, height = 900,
                    ambient = color.gray(0.2),      # Color of non-directional/ambient light
                    background = color.black,       # Color to fill the canvas
                    center = vector(0, 0, 0),
                    fillscreen = True,
                    resizable = True,
                    visible = True,
                )

    def cartAxis(self):
        """ Cartesian Coordinates """
        xaxis = cylinder(pos=vector(0, 0, 0), axis=vector(1, 0, 0), radius=0.01, length=UNIT )
        yaxis = cylinder(pos=vector(0, 0, 0), axis=vector(0, 1, 0), radius=0.01, length=UNIT )
        zaxis = cylinder(pos=vector(0, 0, 0), axis=vector(0, 0, 1), radius=0.01, length=UNIT )
        xlabel = label(text="x-axis", pos=xaxis.axis, font="sans", space=xaxis.radius )
        ylabel = label(text="y-axis", pos=yaxis.axis, font="sans", space=yaxis.radius )
        zlabel = label(text="z-axis", pos=zaxis.axis, font="sans", space=zaxis.radius )


class Assets(Universe):
    def __init__(self):
        Universe.__init__(self)

        self.ball = sphere(
                    pos = vector(0.5, 2*UNIT, 0.5),
                    color = color.red,
                    radius = 0.1,
                )

        self.floor = box(
                    pos = vector(0, 0, 0),
                    color = color.green,
                    size = vector(2*UNIT, 0.01, 2*UNIT)
                )

class InitialConditions(Assets):
    def __init__(self):
        """ Setting up initial conditions """
        Assets.__init__(self)

        self.g = vector(0, -9.8, 0)
        self.dt = 0.01
        self.t = 0

        self.rho = 2.25
        self.coeff = 0.75       # drag coefficient

        self.beta = 0.200

        self.ball.mass = 0.250
        self.ball.initVelocity = vector(0, 0, 0)
        self.ball.finVelocity = self.ball.initVelocity + ( self.g * self.t )    # v = u + at
        self.ball.momentum = self.ball.mass * self.ball.finVelocity
        self.ball.kinetic = ( mag(self.ball.momentum)**2 ) / (2 * self.ball.mass)
        self.ball.potential = self.ball.mass * mag(self.g) * ( self.ball.pos.y - self.floor.pos.y )
        self.ball.weight = self.ball.mass * self.g

        self.contactArea = 2 * np.pi * self.ball.radius**2

class Events(InitialConditions):
    def __init__(self):
        """ Physics Phenomena Simulation """
        InitialConditions.__init__(self)

        trail = curve(color=color.white)
        posgraph = gcurve(color=color.cyan)
        pvector = arrow(pos=self.ball.pos, axis=self.ball.momentum)
        sleep(2)
        print("Time\tKinetic\tPotential\t")

        while ( self.t < 20 ):
            rate(60)
            trail.append(pos=self.ball.pos, retain=2)
            posgraph.plot(pos=(self.t, self.ball.pos.y))
            pvector.pos = self.ball.pos
            pvector.axis = self.ball.momentum * SCALE_DW

            if mag(self.ball.momentum) == 0:
                NORM = 1.0
            elif mag(self.ball.momentum) != 0:
                    NORM = 0.0
            # force due to resistive friction/drag of atmosphere
            self.fdrag = - ( 0.5 * self.coeff * self.rho * self.contactArea * 
                                        mag(self.ball.momentum/self.ball.mass)**2 * 
                                        (self.ball.momentum/( mag(self.ball.momentum) + NORM)) )
            # force that causes energy losses as sound, heat, deformation
            self.fdump = - (self.beta * (self.ball.momentum/self.ball.mass) )
            # net force acting on the ball
            self.fnet = self.ball.weight + self.fdrag + self.fdump

            # Update Ball's porperties
            self.ball.pos += ((self.ball.momentum/self.ball.mass) * self.dt)
            self.ball.momentum += ( self.fnet * self.dt )
            self.ball.kinetic = ( mag(self.ball.momentum)**2 ) / (2 * self.ball.mass)
            self.ball.potential = self.ball.mass * mag(self.g) * ( self.ball.pos.y - self.floor.pos.y )
            self.t += self.dt

            # Change direction upon a bounce
            if ( self.ball.pos.y < (self.floor.pos.y + self.ball.radius) ):
                self.ball.momentum.y = -self.ball.momentum.y

            print("{}s\t{}J\t{}J\t{}m".format(self.t, self.ball.kinetic, self.ball.potential, self.ball.pos.y))

Events()
