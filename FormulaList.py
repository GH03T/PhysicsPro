import math

gravity = 9.8

def momentum(mass, velocity):
    return mass * velocity

def Work(force, displacement, angle):
    return force * displacement * math.cos(angle)

def ForceGravity(mass):
    return mass * gravity

def PotentialEnergy(mass, height):
    return mass * gravity * height

def KineticEnergy(mass, velocity):
    return(1/2 * mass * math.pow(velocity, 2))

