#!/usr/bin/env python3
"""Module that defines the square class"""


class Square:
    """a square with a private size attribute"""

    def __init__(self, size: int = 0) -> None:
        """
            initialize a square instance
        args:
            size of type int: size of the square
        """
        self.size = size

    @property
    def size(self) -> int:
        """return the size attribute"""
        return self.__size

    @size.setter
    def size(self, value):

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """return area of a square"""
        return self.__size ** 2

    def my_print(self):
        if self.size <= 0:
            print()
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="")
            print()
