#!/usr/bin/env python3

from __future__ import division
import vpython as vp
import numpy as np
from time import sleep, time
from vpython import *

UNIT = 1.0
NORM = 1.0
SCALE_UP = 1.30
SCALE_DW = 0.30

class Universe:
    def __init__(self):

        # Universal Constants
        self.G = 6.67e-11
        self.g = vector(0, -9.80665, 0)
        
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
        xaxis = cylinder(pos=vector(0, 0, 0), axis=vector(1, 0, 0), radius=0.1, length=200*UNIT )
        yaxis = cylinder(pos=vector(0, 0, 0), axis=vector(0, 1, 0), radius=0.1, length=200*UNIT )
        zaxis = cylinder(pos=vector(0, 0, 0), axis=vector(0, 0, 1), radius=0.1, length=200*UNIT )
        xlabel = label(text="x-axis", pos=xaxis.axis, font="sans", space=xaxis.radius )
        ylabel = label(text="y-axis", pos=yaxis.axis, font="sans", space=yaxis.radius )
        zlabel = label(text="z-axis", pos=zaxis.axis, font="sans", space=zaxis.radius )

class Assets(Universe):
    def __init__(self):
        """ Physical objects in the universe """
        Universe.__init__(self)

        self.star = sphere(
            pos = vector(0, 0, 0),
            color = color.yellow,
            radius = UNIT,
            opacity = 0.8,
            emissive = True,
            make_trail = True,
            trail_type = "points",
            trail_color = color.red,
            interval = 1000,
            mass = 5e10
        )

        self.planet = sphere(
            pos = vector(12, 0, 0),
            color = color.cyan,
            radius = UNIT/2,
            make_trail = True,
            trail_type = "curve",
            trail_color = color.green,
            mass = 5e10
        )

class InitialConditions(Assets):
    def __init__(self):
        """ Setting up initial conditions in the universe """
        Assets.__init__(self)

        self.dt = 0.01
        self.t = 0

        self.star.initVelocity = vector(0.3, -0.1, 0.3)
        self.planet.initVelocity = vector(-0.3, 0.1, -0.3) #(-0.1, 0, 0.3)

        self.distVect = self.star.pos - self.planet.pos
        self.fgrav = self.G * (self.star.mass * self.planet.mass) * (self.distVect / mag(self.distVect)**3)

        self.star.momentum = (self.star.mass * self.star.initVelocity) + (self.fgrav * self.dt)
        self.planet.momentum = (self.planet.mass * self.planet.initVelocity) + (self.fgrav * self.dt)

        self.star.finVelocity = self.star.momentum / self.star.mass
        self.planet.finVelocity = self.planet.momentum / self.planet.mass

class Events(InitialConditions):
    def __init__(self):
        """ Physics event simulation """
        InitialConditions.__init__(self)

        while (True):
            rate(1000)

            # Calculate force of gravity between the two masses
            self.distVect = self.star.pos - self.planet.pos
            self.fgrav = self.G * (self.star.mass * self.planet.mass) * (self.distVect / mag(self.distVect)**3)

            # Update properties
            self.star.momentum += -self.fgrav * self.dt
            self.planet.momentum += self.fgrav * self.dt

            self.star.pos += (self.star.momentum/self.star.mass) * self.dt
            self.planet.pos += (self.planet.momentum/self.planet.mass) * self.dt

            self.star.finVelocity = self.star.momentum / self.star.mass
            self.planet.finVelocity = self.planet.momentum / self.planet.mass

            self.t += self.dt

            # Upon collision
            if ( mag(self.distVect) <= (self.star.radius + self.planet.radius) ):
                # elastic collision
                self.star.momentum = -self.star.momentum
                self.planet.momentum = -self.planet.momentum

                # inelastic collision
                # self.star.finVelocity = (self.star.momentum + self.planet.momentum) / (self.star.mass + self.planet.mass)
                # self.planet.finVelocity = (self.star.momentum + self.planet.momentum) / (self.star.mass + self.planet.mass)
                # self.star.momentum = self.star.mass * self.star.finVelocity
                # self.planet.momentum + self.planet.mass * self.planet.finVelocity

Events()