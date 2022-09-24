# rigidbody parent class implementation
from pyglet.math import *

class RigidBody:
    # parent class to derieve from
    def __init__(self,
        x,                       # [m] position
        mass = 1,                # [kg] mass
        v0 = Vec2(),             # [m s⁻¹] initial velocity
        color = (255, 255, 255), # color; white
        batch = None,
    ):
        self.x = x   # [m] position
        self.x0 = x  # [m] previous position
        self.v = v0  # [m s⁻¹] velocity
        self.a = 0   # [m s⁻²] acceleration

        self.m = mass       # [kg] mass
        self.m_i = 1 / mass # [kg⁻¹] reciprocal of mass

        self.cor = 1  # coefficient of restitution

        self.color = color
        self.shape = None  # note: change this to the shape in inherited class


    def apply_forces(self,
            *forces, # [N] the forces to apply
        ):
        if not forces: return
        # find net force and add
        self.a = self.a + sum(forces) * self.m_i

    
    def update(self,
        dt, # [s] difference in time
    ):
        # save the position
        save_x = self.x
        # update position with the previous position
        self.x = self.x + (self.x - self.x0)
        # euler's method amiright
        # maybe use a different method, maybe RK4
        # RK4 ref: https://www.haroldserrano.com/blog/visualizing-the-runge-kutta-method
        # https://gafferongames.com/post/integration_basics/
        # in simple words: multiply by dt to remove the time term
        # [m]     = [m s⁻¹] × [s]
        # [m s⁻¹] = [m s⁻²] × [s]
        self.x = self.x + self.v.scale(dt)
        self.v = self.v + self.a.scale(dt)
        # set previous position to the saved (unupdated) position
        self.x0 = save_x

        # reset acceleration
        self.a = Vec2()

        # note: update the shapes in the inherited class


    # NotImplemented stuff, the children should implement it
    collide = collide_border = draw = lambda self: 1 / 0  # divide by zero to raise exception lol
