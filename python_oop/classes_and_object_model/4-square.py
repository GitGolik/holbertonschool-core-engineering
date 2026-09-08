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
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """return area of a square"""
        return self.__size ** 2

    def size(self) -> int:
        """return the size attribute"""
        return self.__size
