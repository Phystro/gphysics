#!/usr/bin/env python3 

import numpy as np
import matplotlib.pyplot as plt

G = 6.67e-11
M = 5.97e24
R = 6371000

class SatAlt:
    def __init__(self):

        # arrays for variables to draw graph
        self.time_values = []
        self.altt_values = []

        # input period time to get sat altitude
        self.period = float(input("Enter Period Time of Satellite: "))
        self.print_results("Satellite", self.period, self.get_altitude(self.period)) 

        # geosynchronous sats 
        tt = 86400
        self.print_results("Geosynchronous Satellites", tt, self.get_altitude(tt))

        # geo-sat using sidereal day
        tt = 23.98 * 3600
        self.print_results("Geosynchronous Satellites Using Sidereal Day", tt, self.get_altitude(tt))

        # 90 minute sats
        tt = 90 * 60
        self.print_results("90 Minute Period Satellites", tt, self.get_altitude(tt))

        # 45 minute sats
        tt = 45 * 60
        self.print_results("45 Minute Period Satellites", tt, self.get_altitude(tt))

        # graph window
        win = plt.figure()

        # sort the plotting values from the lowest to the highest
        self.time_values.sort()
        self.altt_values.sort()

        # draw the plot
        graph = plt.plot(self.time_values, self.altt_values, "ro-", color="black")
        plt.title("Satellite Period Time vs Satellite Altitude")
        plt.xlabel("Period Time (s)")
        plt.ylabel("Altitude (m)")
        plt.grid()
        plt.show()
    

    def get_altitude(self, t):
        coeff = (G*M) / (4*np.pi**2)
        coeff = pow(coeff, 1/3)

        h = ( coeff * pow(t**2, 1/3) ) - R

        return h


    def print_results(self, category, time, altitude):
        print("{}:".format(category))
        print("\tPeriod Time\t: {:,} [s]\t:= {:,.3f} [hrs]".format( time, time/3600 ))
        print("\tAltitude\t: {:,.3f} [m]".format(altitude)) if (altitude > 0) else print("\t[-] Period Time too short to maintain a satellite above the Earth's surface")
        print("\n\r")

        # fill in array
        self.time_values.append(time)
        self.altt_values.append(altitude)


SatAlt()
