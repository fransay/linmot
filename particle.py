"""
particle type for linear motion.
mass and volume of particle are negligible.
"""
from utils.generics import delta


class Particle(object):
    """
    standard symbols for quantities
    initial velocity (u)
    final velocity (v)
    """
    def __int__(self, initial_velocity, final_velocity, duration_in_seconds):
        self.init_velocity = initial_velocity
        self.fin_velocity = final_velocity
        self.dur = duration_in_seconds

    def acceleration(self):
        """
        acceleration of a particle is the change in velocity over a period of time.
        :return:
        """
        acceleration = delta(self.init_velocity, self.fin_velocity) / self.dur
        return acceleration

    def linear_distance(self):
        """
        returns the linear distance(s) using the equation (v^2 - u^2)/2a
        :return:
        """
        lin_dist = (self.final_velocity**2 - self.init_velocity**2) / 2 * self.acceleration()
        return lin_dist


