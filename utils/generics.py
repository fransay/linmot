from math import sqrt as s

"""
standalone functions 
"""


def delta(quantity_A, quantity_B):
    """
    return the non-absolute difference between two quantities
    :param quantity_A:
    :param quantity_B:
    :return:
    """
    out = quantity_B - quantity_A
    return out


def linear_velocity(delta_displacement, delta_time):
    """
    returns linear velocity given the linear change in displacement over a period of time
    :param delta_displacement:
    :param delta_time:
    :return:
    """
    return delta_displacement


def displacement_coordinates(point_A: tuple, point_B: tuple):
    """
    point struct: (x,y)
    returns the linear displacement of a particles given an initial and final positions.
    position is expressed in cartesian coordinates
    :param point_A:
    :param point_B:
    :return:
    """
    disp = s((point_B[0] - point_A[0]) ** 2 + (point_B[1] - point_A[1]) ** 2)
    return disp


def initial_velocity(final_velocity, acceleration, time_duration):
    """
    returns final velocity(v) as v = u + at
    :param final_velocity:
    :param acceleration:
    :param time_duration:
    :return:
    """
    return final_velocity - (acceleration * time_duration)


def final_velocity(initial_velocity, acceleration, time_duration):
    """
    returns final velocity(v) as v = u + at
    :param initial_velocity:
    :param acceleration:
    :param time_duration:
    :return:
    """
    return initial_velocity + (acceleration * time_duration)


def time_duration(initial_velocity, final_velocity, acceleration):
    """
    retn
    :param initial_velocity:
    :param final_velocity:
    :param acceleration:
    :return:
    """
    time_durationn = delta(initial_velocity, final_velocity) / acceleration
    return time_durationn


def jerk(acceleration, time_duration):
    """
    jerk is the rate of change acceleration,
    can be computed from the third order derivative of acceleration
    :param acceleration:
    :param time_duration:
    :return:
    """
    return acceleration/time_duration


def jounce(jerk, time_duration):
    """
    jounce is the rate of change of jerk,
    can be computed from the fourth order derivative of acceleration
    :param jerk:
    :param time_duration:
    :return:
    """
    return jerk/time_duration


