#!/usr/bin/env python3

from vpython import *
import vpython as vp

L = 4
Rs = 0.25       # radius of sodium atom
Rc = 0.50       # radius of chlorine atom

alt = 1         # alternating factor

for i in range(-L, L+1):
    for j in range(-L, L+1):
        for k in range(-L, L+1):
            if alt == 1:
                atom_Na = sphere(pos=vector(i, j, k), radius=Rs, color=color.purple)
            elif alt  == -1:
                atom_Cl = sphere(pos=vector(i, j, k), radius=Rc, color=color.green)
            
            alt *= -1


