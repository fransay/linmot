"""
Points are essential in particle physics
simple point type created
"""


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def point_tupled(self):
        """
        tuple representation of point
        :return:
        """
        return self.x, self.y

    def point_listed(self):
        """
        list representation of point
        :return:
        """
        return [self.x, self.y]

    def point_hashed(self):
        """
        dictionary representation of point
        :return:
        """
        return {"x": self.x, "y": self.y}
