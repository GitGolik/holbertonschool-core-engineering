#!/usr/bin/env python3
"""Module defining besegeometry class"""


BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class of rectangle geometric shape"""

    def __init__(self, width, height):
        """setting rectangle attributes"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
