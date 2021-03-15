"""
NOTE: Observe SI units
"""

import numpy as np
import matplotlib.pyplot as plt
from time import sleep

# constants
PI = np.pi
gravity = 9.81
time_delta = 0.1
thrust = 800

class ObjectSpecs:
    def __init__(self):
        """Physical objects involved, their characteristics and properties/specifications"""
        
        # Rocket Specs
        self.mass_rocket = 5    # [kg]
        self.mass_fuel = 21     # [kg]
        self.mass_total = self.mass_fuel + self.mass_rocket # [kg]
        # self.thrust = 1300.0    # 
        self.thrust = thrust
        self.rate_consumption = 0.0584     # fuel burn rate [kg/s]
        self.effective_surface_radius = 0.1     # effective surface radius exposed to drag effects [m]

class InitialConditions(ObjectSpecs):
    def __init__(self):
        ObjectSpecs.__init__(self)

        # initial conditions
        self.time_init = 0.0
        self.height_init = 0.0000000001
        self.velocity_init = 0.0
        self.acceleration_init = 0.0

        self.time = self.time_init
        self.time_delta = time_delta

        self.gravity = gravity
        self.height = self.height_init
        self.velocity = self.velocity_init
        self.acceleration = self.acceleration_init

        # arrays for collecting telemetry data
        self.bins_time = []
        self.bins_height = []
        self.bins_velocity = []
        self.bins_acceleration = []
        self.bins_mass = []


class Physics:
    def __init__(self):
        pass
    def get_gravity(self, h):
        """Computes and returns value of gravitational acceleration. Gravitational acceleration varies with height from the Earth's surface."""
        g = gravity / (1 + h/6371000)
        return g

    def get_drag_coeff(self):
        """Assuming a constant drag coefficient.
        Realistically, it would vary with height."""
        drag_coefficient = 0.1  # for a well streamlined body
        return drag_coefficient


class Simulation(InitialConditions):
    def __init__(self):
        InitialConditions.__init__(self)

        while (self.height >= 0.0):

            self.gravity = Physics().get_gravity(self.height)
            self.get_mass_total(self.time)
            self.get_thrust()
            self.get_acceleration()
            self.update_velocity()
            self.update_height()

            # print(self.time, "\t\t", self.mass_total, "\t\t", self.mass_fuel, "\t\t", self.mass_rocket, "\t\t", self.height)

            # fill in telemetry data into arrays
            self.bins_time.append(self.time)
            self.bins_height.append(self.height)
            self.bins_mass.append(self.mass_fuel)
            self.bins_velocity.append(self.velocity)
            self.bins_acceleration.append(self.acceleration)

            self.inc_time()
            # sleep(1)

        print("TOUCHDOWN!")
        self.plot_graphs()
        

    def get_thrust(self):
        if self.mass_fuel <= 0:
            self.thrust = 0.0
            self.mass_fuel = 0.0
            self.mass_total = self.mass_fuel + self.mass_rocket
            # print("[-] OUT-OF-FUEL! NO THRUST AVAILABLE!")
        else:
            self.thrust = thrust
        return self.thrust

    def get_mass_total(self, time):
        if self.mass_total >= self.mass_rocket:
            self.mass_fuel -= ( self.rate_consumption * time )
            self.mass_total = self.mass_rocket + self.mass_fuel
        return self.mass_total

    def get_drag(self, h, velocity):
        area_surface = 0.25 * PI * (self.effective_surface_radius**2)
        drag_coeff = Physics().get_drag_coeff()

        # TODO: implement ISA atmosphere model
        atm_density = 1.225     # kg/m^3

        drag = 0.5 * drag_coeff * atm_density * area_surface * velocity**2
        return drag

    def get_acceleration(self):
        if self.mass_total >= self.mass_rocket:
            # thrust = self.get_thrust()
            # mass = self.get_mass_total(t)
            drag = self.get_drag(self.height, self.velocity)

            self.acceleration = ( self.thrust - self.mass_total*self.gravity - drag ) / self.mass_total # from Newton's second law

        return self.acceleration

    def update_height(self):
        self.height += self.velocity * self.time

    def update_velocity(self):
        self.velocity = self.velocity_init + ( self.acceleration * self.time )

    def plot_graphs(self):
        fig, ( (gr_mass, gr_height), (gr_velocity, gr_acceleration) ) = plt.subplots(nrows=2, ncols=2, sharex=True)

        gr_mass.set_title("Rocket Fuel Mass (kg) vs Time (s)")
        gr_mass.set_xlabel("Time (s)")
        gr_mass.set_ylabel("Fuel Mass (kg)")
        gr_mass.grid()

        gr_height.set_title("Height (m) vs Time (s)")
        gr_height.set_xlabel("Time (s)")
        gr_height.set_ylabel("Height (m)")
        gr_height.grid()

        gr_velocity.set_title("Velocity $(m/s)$ vs Time $(s)$")
        gr_velocity.set_xlabel("Time $(s)$")
        gr_velocity.set_ylabel("Velocity $(m/s)$")
        gr_velocity.grid()

        gr_acceleration.set_title("Acceleration $(m/s^2)$ vs Time $(s)$")
        gr_acceleration.set_xlabel("Time $(s)$")
        gr_acceleration.set_ylabel("Acceleration $(m/s^2)$")
        gr_acceleration.grid()

        gr_mass.plot(self.bins_time, self.bins_mass, label="mass")
        gr_height.plot(self.bins_time, self.bins_height, label="Height")
        gr_velocity.plot(self.bins_time, self.bins_velocity, label="Velocity")
        gr_acceleration.plot(self.bins_time, self.bins_acceleration, label="Acceleration")

        gr_mass.legend()
        gr_height.legend()
        gr_velocity.legend()
        gr_acceleration.legend()

        fig.suptitle("Single-Stage Rocket Simulation Telemetry Data")
        fig.set_dpi(800)

        plt.savefig("images/single_stage_rocket_telemetry.png", dpi=800)
        plt.savefig("images/single_stage_rocket_telemetry.svg", dpi=800)

        plt.show()
        plt.close()

    def inc_time(self):
        self.time += self.time_delta


Simulation()