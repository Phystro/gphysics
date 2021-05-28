#!/usr/bin/env python3

from __future__ import division
import vpython as vp
from vpython import *
from numpy import pi, arange, cos, sin
from time import sleep

MEGA = 1e9 # a million
KILO = 1e5    # multiplier for planet visibility
TF = pi      # animation time factor
PT = 1e6    # evolution/simulation periodic time

# update position
def update_position(obj, angle):
    obj.pos.x = cos(angle/orbit_period[obj])
    obj.pos.y = sin(angle/orbit_period[obj])
    obj.pos.z = 0

    return obj.pos

# set the scene
scene = vp.canvas(
        title="Solar System",
        x = 0, y = 0,
        width=1600, height=900,
        resizable=True,
        visible=True)


# initialize objects
sun = sphere(
    name="Sun",
    pos=vector(0, 0, 0),
    color=color.yellow,
    radius=695500*KILO/2,
    opacity=1.0,
    emissive=True)

mercury = sphere(
    name="Mercury",
    pos=vector(57.9*MEGA, 0, 0),
    color=vector(0.54, 0.57, 0.57),
    radius=2440*KILO,
    opacity=0.96,
    make_trail=True,
    retain=500,
    trail_color=vector(0.54, 0.57, 0.57))

venus = sphere(
    name="Venus",
    pos=vector(108.2*MEGA, 0, 0), 
    color=color.orange, 
    radius=6052*KILO, 
    opacity=0.95,
    make_trail=True,
    retain=500,
    trail_color=color.orange)

earth = sphere(
    name="Earth",
    pos=vector(149.6*MEGA, 0, 0), 
    color=color.cyan, 
    radius=6371*KILO, 
    opacity=0.95, 
    make_trail=True,
    retain=500,
    trail_color=color.cyan)

mars = sphere(
    name="Mars",
    pos=vector(227.9*MEGA, 0, 0), 
    color=color.red, 
    radius=3386*KILO, 
    opacity=0.95, 
    make_trail=True,
    retain=500,
    trail_color=color.red)

jupiter = sphere(
    name="Jupiter",
    pos=vector(778.5*MEGA, 0, 0), 
    color=vector(1.0, 0.64, 0), 
    radius=69173*KILO, 
    opacity=0.9, 
    make_trail=True,
    retain=500,
    trail_color=vector(1.0, 0.64, 0))

saturn = sphere(
    name="Saturn",
    pos=vector(1433.4*MEGA, 0, 0), 
    color=vector(1.0, 0.84, 0), 
    radius=57316*KILO, 
    opacity=0.9, 
    make_trail=True,
    retain=500,
    trail_color=vector(1.0, 0.84, 0))

uranus = sphere(
    name="Uranus",
    pos=vector(2871.0*MEGA, 0, 0), 
    color=color.green, 
    radius=25559*KILO, 
    opacity=0.9, 
    make_trail=True,
    retain=500,
    trail_color=color.green)

neptune = sphere(
    name="Neptune",
    pos=vector(4497.1*MEGA, 0, 0), 
    color=color.blue, 
    radius=24300*KILO, 
    opacity=0.9, 
    make_trail=True,
    retain=500,
    trail_color=color.blue)

# make array of spheres
system = [sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]
radii = {sun:0, mercury:57.9*MEGA, venus:108.2*MEGA, earth:149.6*MEGA, mars:227.9*MEGA, jupiter:778.5*MEGA, saturn:1433.4*MEGA, uranus:2871.0*MEGA, neptune:4497.1*MEGA}
orbit_period = {sun:1, mercury:87.96, venus:224.68, earth:365.26, mars:686.98, jupiter:4332.71, saturn:10759.10, uranus:30707.41, neptune:90474.90}

# Labels
for obj in system:
    label( pos=obj.pos, text=obj.name, font="sans", border=0, box=False, color=obj.color )

# animation
t = 0
dt = 2*TF
sleep(5)        # wait for animation to start
while ( t < PT ):
    rate(30)

    for obj in system:
        obj.pos = radii[obj] * update_position(obj, t)
 
    t += dt
