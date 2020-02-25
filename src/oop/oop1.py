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
    pass

# Vehicle is parent and GroundVehicle is child


class GroundVehicle(Vehicle):
    pass


# GroundVehicle is parent and Car is a child
class Car(GroundVehicle):
    pass

# GroundVehicle is the parent and Motorcycle is a child


class Motorcycle(GroundVehicle):
    pass

# FlightVehicle is a child class of Vehicle


class FlightVehicle(Vehicle):
    pass


# Airplane inherits from FlightVehicle
class Airplane(FlightVehicle):
    pass

# Starship inherits from FlightVehicle


class Starship(FlightVehicle):
    pass
