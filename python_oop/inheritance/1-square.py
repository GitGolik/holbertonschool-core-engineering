#!/usr/bin/env python3
"""Module for a square"""


Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """defining the square attributes"""

    def __init__(self, size):
        """create a square"""

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
