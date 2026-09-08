#!/usr/bin/env python3
"""Module that defines the square class"""


class Square:
    """a square with a private size attribute"""

    def __init__(self, size: int) -> None:
        """
        initialize a square instance

        args:
            size of type int: size of the square
        """
        self.__size = size
