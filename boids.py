# Jackson Morgan, Sam Groom
# Boids Algorithm - Classes and Functions

import math
import random

class boid:
    def __init__(self, world, v_max):

        self.name = None # empty attribute to be filled later

        # boid gets random location in boid world:
        self.x = random.uniform(-world[0], world[0])
        self.y = random.uniform(-world[1], world[1])
        self.z = random.uniform(-world[2], world[2])

        # boid gets random velocity <= max velocity and in random direction
        v_dir_x = random.uniform(0, 2 * math.pi) # velocity vector angle from x-axis
        v_dir_y = random.uniform(0, 2 * math.pi) # velocity vector angle from y-axis
        v_dir_z = random.uniform(0, 2 * math.pi) # velocity vector angle from z-axis
        v_mag = random.uniform(0, v_max)
        self.vx = v_mag * math.cos(math.pi/4 - v_dir_z) * math.cos(v_dir_x)
        self.vy = v_mag * math.cos(math.pi/4 - v_dir_z) * math.cos(v_dir_y)
        self.vz = v_mag * math.cos(v_dir_x) * math.cos(v_dir_z)

class flock:
    def __init__(self, S, world, v_max):
        self.members = [boid(world, v_max) for i in range(S)]

        # give each boid unique identifier so we can sort them and then re-sort them when giving states to animation:
        # ---- not sure why we'd need to sort them, just remember waking up at 4 AM last night and thinking we'd need to for some reason ----
        for i in range(S):
            self.members[i].name = int(i)


    def update_state(self, world, k):

        # Seperation

        # Alignment

        # Cohesion

        # Predator Avoidance

        # update location
        for i in range(len(self.members)):
            boid = self.members[i]
            boid.x = boid.x + boid.vx * k
            boid.y = boid.y + boid.vy * k
            boid.z = boid.z + boid.vz * k
        
            if boid.x > world[0]:
                boid.x = boid.x - 2 * world[0]
            elif boid.x < -world[0]:
                boid.x = boid.x + 2 * world[0]
            elif boid.y > world[1]:
                boid.y = boid.y - 2 * world[1]
            elif boid.y < -world[1]:
                boid.y = boid.y + 2 * world[1]
            elif boid.z > world[2]:
                boid.z = boid.z - 2 * world[2]
            elif boid.z < -world[2]:
                boid.z = boid.z + 2 * world[2]

'''
class hawk:
    def __init__(self, ):
'''


