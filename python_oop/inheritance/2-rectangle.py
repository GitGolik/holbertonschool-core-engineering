#!/usr/bin/env python3
"""Module defining area and str of the rectangle"""


Rectangle = __import__('1-rectangle').Rectangle


class Rectangle(Rectangle):
    """Represent a rectangle"""

    def area(self):
        """return the area of the rectangle"""

        return self._Rectangle__width * self._Rectangle__height

    def __str__(self):
        """return the rectangle description"""

        return "[Rectangle] {}/{}".format(
            self._Rectangle__width,
            self._Rectangle__height
        )
