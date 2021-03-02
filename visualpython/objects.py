#!/usr/bin/env python3

from __future__ import division
import vpython as vp


# CANVAS
scene = vp.canvas(
            fullscreen = True
        )


# GRAPH WINDOW
gr = vp.graph(
            title = "Graph Window Objects",
            x = 0, y = 0,
            xtitle = "x_title", ytitle="y_title",
            background  =vp.color.white
        )


# RED BOX
redbox = vp.box(
            pos = vp.vector(4, 2, 3),
            size = vp.vector(8, 4, 6),
            color = vp.color.red
        )
