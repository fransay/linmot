"""
particle type for linear motion.
mass and volume of particle are negligible.
"""
from utils.generics import delta


class Particle(object):
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
        linear s
        :return:
        """
