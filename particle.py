"""
particle type for linear motion.
mass and volume of particle are negligible.
fundamental equation of
"""
from utils.generics import delta


class Particle(object):
    """
    standard symbols for quantities
    initial velocity (u)
    final velocity(v)
    time duration(t)
    linear distance(s)

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

    def linear_distance_type1(self):
        """
        returns the linear distance(s) using the equation s = (v^2 - u^2)/2a
        where all variable in equation assume their standard meaning
        :return:
        """
        lin_dist = (self.final_velocity ** 2 - self.init_velocity ** 2) / 2 * self.acceleration()
        return lin_dist

    def linear_distance_type2(self):
        """
        returns the linear distance(s) using the equation s = ut  + 1/2at^2
        where all variable in equations assume their standard meaning
        :return:
        """
        lin_dist = (self.init_velocity * self.dur) + (self.acceleration() * self.dur ** 2) / 2
        return lin_dist

    def linear_velocity(self, initial_time, final_time):
        """
        returns the linear distance given the initial and final time
        :param initial_time:
        :param final_time:
        :return:
        """
        change_in_time = delta(initial_time, final_time)
        change_in_velocity = delta(self.init_velocity, self.fin_velocity)
        return change_in_velocity/change_in_time

    # include setter methods

    def set_new_initial_velocity(self, new_initial_velocity):
        """
        set old initial velocity to new initial velocity
        """
        self.init_velocity = new_initial_velocity

    def set_new_final_velocity(self, new_final_velocity):
        """
        set old final velocity to new initial velocity
        """
        self.fin_velocity = new_final_velocity

    def set_new_time_duration_in_seconds(self, new_time_duration):
        """
        set old time duration to new time duration
        time must be in seconds
        """
        self.dur = new_time_duration





