#!/usr/bin/env python3
"""Module defining besegeometry class"""


class BaseGeometry:
    """Base class for geometric figure"""

    def area(self):
        """raise an exception because area is still not implemented"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate that value is a positive int"""

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
