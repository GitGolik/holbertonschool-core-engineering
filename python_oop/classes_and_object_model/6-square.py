#!/usr/bin/env python3
"""Module that defines a Square class."""




class Square:
    """Represent a square with a size and a position."""


    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square with a size and a position."""
        self.size = size
        self.position = position


    @property
    def size(self):
        """Get the size of the square."""
        return self.__size


    @size.setter
    def size(self, value):
        """Set the size of the square after validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value


    @property
    def position(self):
        """Get the position of the square."""
        return self.__position


    @position.setter
    def position(self, value):
        """Set the position of the square after validation."""
        if (
                not isinstance(value, tuple)
                or len(value) != 2
                or not all(isinstance(item, int) for item in value)
                or not all(item >= 0 for item in value)
        ):
            raise TypeError(
                "position must be a tuple of 2 positive integers"
            )
        self.__position = value


    def area(self):
        """Return the area of the square."""
        return self.__size ** 2


    def my_print(self):
        """Print the square using the character '#'."""
        if self.__size == 0:
            print()
            return


        # lignes vides avant le carré (position[1])
        for _ in range(self.__position[1]):
            print()


        # chaque ligne du carré
        spaces = " " * self.__position[0]
        line = spaces + "#" * self.__size


        for _ in range(self.__size):
            print(line)


    def __str__(self):
        """Return the square as a string made of '#' characters."""
        if self.__size == 0:
            return ""


        spaces = " " * self.__position[0]
        line = spaces + "#" * self.__size


        # on construit juste les lignes du carré, pas de sauts de ligne vides
        return "\n".join([line for _ in range(self.__size)])
