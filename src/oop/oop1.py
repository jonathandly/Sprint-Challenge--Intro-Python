# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


# Vehicle is the base class that all other classes inherit from.
class Vehicle:
    def __init__(self, num_wheels):
        self.num_wheels = num_wheels


# FlightVehicle is a child class of Vehicle
class FlightVehicle(Vehicle):
    pass

# Starship inherits from FlightVehicle


class Starship(FlightVehicle):
    pass
