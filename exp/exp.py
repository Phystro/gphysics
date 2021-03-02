#!/usr/bin/env python3

from __future__ import division
import numpy as np
from vpython import *
import vpython as vp


class Universe:
    def __init__(self):

        self.viewScene()
        self.cartAxis()

        # Constants
        self.g = 9.80665

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

