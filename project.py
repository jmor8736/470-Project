# Jackson Morgan, Samuel Groom
# Boids Algorithm - Implementation

import math
import boids
import numpy as np
from vpython import *

sky_blue = vec(.45, .785, 1)
light_gray = vec(.8, .8, .8)
scene = canvas(width=1260, height=600, background=sky_blue)

world = [15, 15, 15] # defines the size of the world that boids will exist in
S = 10 # number of boids
v_max = 2 # maximum velocity of boids
size = [0.5, 3] # size of boid [radius, length]
k = 1 # time step size
n = 1000 # number of time steps

flock = boids.flock(S, world, v_max)

# initialize animation:
objects = []
for i in range(S):
    boid = flock.members[i]
    position = vec(boid.x, boid.y, boid.z)
    mag = math.sqrt(boid.vx**2 + boid.vy**2 + boid.vz**2)
    dir = vec(boid.vx/mag, boid.vy/mag, boid.vz/mag)
    len = size[1]
    rad = size[0]
    objects.append(cone(pos=position, axis=dir, radius=rad, length=len))


for i in range(n):
    flock.update_state(world, k)

    for j in range(S):
        boid = flock.members[j]
        position = vec(boid.x, boid.y, boid.z)
        mag = math.sqrt(boid.vx**2 + boid.vy**2 + boid.vz**2)
        dir = vec(boid.vx/mag, boid.vy/mag, boid.vz/mag)
        len = size[1]
        rad = size[0]
        rate = (10000)
        objects[j].pos = position
        objects[j].axis = dir




