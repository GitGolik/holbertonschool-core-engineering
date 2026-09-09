#!/usr/bin/env python3
"""Module of square of str"""


Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """create a square"""

    def __init__(self, size):
        """initialize a square"""

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """return the square desc"""

        return "[Square] {}/{}".format(
            self._Rectangle__width,
            self._Rectangle__height
        )
