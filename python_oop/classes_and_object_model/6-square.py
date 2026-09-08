#!/usr/bin/env python3
"""Module that defines the Square class with size and position."""


class Square:
    """Represents a square with size and position attributes."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a Square instance.

        Args:
            size (int): The size of the square.
            position (tuple): A tuple of 2 positive integers (x, y).

        Raises:
            TypeError: If size is not an integer or position is invalid.
            ValueError: If size < 0 or position values are not positive.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size attribute with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for the position attribute."""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for the position attribute with validation.

        position must be a tuple of 2 positive integers.
        """
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(x, int) for x in value)
            or any(x < 0 for x in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def my_print(self):
        """
        Print the square in stdout using '#' character.

        Uses position to add leading spaces.
        If size == 0, prints an empty line.
        """
        if self.__size == 0:
            print()
            return

        spaces = " " * self.__position[0]
        line = spaces + "#" * self.__size

        for _ in range(self.__size):
            print(line)

    def __str__(self):
        """
        Return a string representation of the square.

        Same behavior as my_print(), but returns a string instead of printing.
        """
        if self.__size == 0:
            return ""

        spaces = " " * self.__position[0]
        line = spaces + "#" * self.__size
        return "\n".join([line for _ in range(self.__size)])
