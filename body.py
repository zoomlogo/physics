# rigidbody implementations
from pyglet.math import *

class RigidBody:  # parent class to derieve from
    def __init__(self,
        x,                       # [m] position
        mass = 1,                # [kg] mass
        v0 = Vec2(),             # [m s⁻¹] initial velocity
        color = (255, 255, 255), # color; white
        batch = None,
    ):
        self.x = x  # [m] position
        self.v = v0 # [m s⁻¹] velocity
        self.a = 0  # [m s⁻²] acceleration

        self.m = mass       # [kg] mass
        self.m_i = 1 / mass # [kg⁻¹] reciprocal of mass

        self.color = color


    def apply_forces(self,
            *forces, # [N] the forces to apply
        ):
        if not forces: return
        # find net force and add
        self.a = self.a + sum(forces) * self.m_i

    
    def update(self,
        dt, # [s] difference in time
    ):
        # euler's method amiright
        # maybe use a different method for polygons or something
        # in simple words: multiply by dt to remove the time term
        # [m]     = [m s⁻¹] × [s]
        # [m s⁻¹] = [m s⁻²] × [s]
        self.x = self.x + self.v * dt
        self.v = self.v + self.a * dt

        # reset acceleration
        self.a = Vec2()


    # NotImplemented stuff, the children should implement it
    collide = collide_border = draw = lambda self: 1 / 0  # divide by zero to raise exception lol
