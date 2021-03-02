#!/usr/bin/env python3

from __future__ import division
import vpython as vp
import numpy as np

# Animation/Simulation scene
scene = vp.canvas(
            x=0, y=0,
            width=800, height = 450
        )
#scene.lights = []   # get rid of default lights

scene.ambient = vp.color.gray(0.2)

# Graph Analytical
win1 = vp.graph(
            x = 700, y = 0,
            width = 800, height = 450,
            title = "Single Simple Pendulum",
            xtitle = "x", ytitle = "y",
            foreground = vp.color.black,
            background = vp.color.white,
            stereo = "redcyan"
        )

# 
initial_position = vp.vector(-4, 0, 0)
initial_velocity = vp.vector(0, 0, 0)


# Define Ball/Blob
ball = vp.sphere(
            pos = initial_position,
            radius = 0.5,
            color = vp.color.cyan,
            opacity = 0.8,
            make_trail = True,
            emissive = False
        )

# Define Rod
rod = vp.cylinder(
            pos = initial_position,
            axis = -ball.pos,
            radius = 0.1
        )

# scene.autoscale = 0

ball.velocity = initial_velocity
ball.mass = 0.1

#scene.camera.follow(ball)

dt = 0.005
t = 0
T = 20
k = 10000                     # Spring Constant
d = 4
g = -9.810655
drag_coefficient = 0.00019 * 0.5


# A plot
kinetic = vp.gcurve(color = vp.color.blue)

while (t < T):
    vp.rate(100)
    relative_displacement = rod.length - d
    ball_force = -k * relative_displacement * ball.pos.norm()
    ball_force.y += g
    ball_force -= drag_coefficient * ball.velocity.mag**2 * ball.velocity
    acceleration = ball_force / ball.mass
    ball.velocity += acceleration * dt

    kinetic_energy = 0.5 * ball.mass * ball.velocity.mag**2
    kinetic.plot(t, kinetic_energy)

    ball.pos += ball.velocity * dt
    rod.pos = ball.pos
    rod.axis = -ball.pos
    t += dt


