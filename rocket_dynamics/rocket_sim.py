"""
NOTE: Observe SI units
"""

import numpy as np
import matplotlib.pyplot as plt

# constants
PI = np.pi
gravity = -9.81
time_delta = 0.01

# initial conditions
time_init = 0.0
height_init = 0.0
velocity_init = 0.0
acceleration_init = 0.0

mass_rocket = 5    # kg
mass_fuel = 20      # kg
thrust = 13000
rate_consumption = 660  # kg/s

class Rocket():
    def __init__(self, mass_rocket, mass_fuel, thrust, rate_consumption):
        self.gravity = gravity
        self.height = height_init
        self.velocity = velocity_init
        self.mass_rocket = mass_rocket
        self.mass_fuel = mass_fuel
        self.mass_total = mass_rocket + mass_fuel
        self.rate_consumption = rate_consumption
        self.thrust = thrust
        self.acceleration = acceleration_init

    def get_thrust(self):
        if self.mass_fuel <= 0:
            thrust = 0.0
        else:
            thrust = 13000.0
        return thrust

    def get_acceleration(self, h, v, t):
        if self.mass_total >= self.mass_rocket:
            g = self.get_gravity(h)
            thrust = self.get_thrust()
            mass = self.get_mass(t)
            drag = self.get_drag(h, v)

            acc = ( thrust - mass*g - drag ) / mass # from Newton's second law
            return acc


    def get_mass(self, time):
        if self.mass_total >= self.mass_rocket:
            self.mass_total = self.mass_rocket + ( self.mass_fuel - ( self.rate_consumption * time ) )
        return self.mass_total

    def get_drag_coeff(self):
        """Assuming a constant drag coefficient.
        Realistically, it would vary with height."""
        drag_coefficient = 0.1  # for a well streamlined body
        return drag_coefficient

    def get_drag(self, h, velocity):
        effective_surface_radius = 0.1      # effective surface area exposed to drag effects
        area_surface = 0.25 * PI * (effective_surface_radius**2)
        drag_coeff = self.get_drag_coeff()
        
        # TODO: implement ISA atmosphere model
        atm_density = 1.225     # kg/m^3

        drag = 0.5 * drag_coeff * atm_density * area_surface * velocity**2
        return drag

    def get_gravity(self, h):
        """Computes and returns value of gravitational acceleration. Gravitational acceleration varies with height from the Earth's surface."""
        g = gravity / (1 + h/6371000)
        return g


class Simulation(Rocket):
    def __init__(self, Rocket):
        Rocket.__init__(self, mass_rocket, mass_fuel, thrust, rate_consumption)

        self.time = time_init
        self.time_delta = time_delta

        bins_time = []
        bins_height = []
        bins_velocity = []
        bins_velocity = []
        bins_mass = []

        while ( self.height >= 0 ):

            self.get_acceleration(self.height, self.velocity, self.time)
            self.update_velocity(self.acceleration)
            self.update_height(self.height)
            print(self.height)
            self.inc_time()


        
    def plot_graphs(self):
        pass

    def update_height(self, h):
        h += self.velocity * self.time
        return h

    def update_velocity(self, a):
        v = self.velocity + a * self.time
        return v

    def inc_time(self):
        self.time += self.time_delta


Simulation(Rocket)
