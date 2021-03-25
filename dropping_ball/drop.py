#!/usr/bin/env python3

import numpy as np

g = 9.81

class Drop:
    def __init__(self):

        self.height = float(input("Enter height of tower [m]: "))
        self.velocity_init = 0
        print("\n\rAnalysis:")
        print("\tInitial Velocity\t: %3.3f [m/s]"%(self.velocity_init))
        print("\tInitial Height\t\t: %3.3f [m]"%(self.height))
        print("\tAir Resistance\t\t: Ignored")
        print("\tTime Taken To Drop\t: %3.3f [s]"%( self.get_time( self.get_vel_from_dist( self.velocity_init, self.height ),  self.velocity_init) ))

    def get_vel_from_dist(self, u, s):
        vv = u**2 + 2*g*s
        return np.sqrt(vv)

    def get_time(self, v, u):
        t = (v - u) / g
        return t

Drop()

