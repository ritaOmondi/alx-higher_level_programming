#!/usr/bin/python3
"""Defining class Square"""


class Square:
    """The class body"""
    def __init__(self, size=0):
        """The constructor
        Args:
        size (integer) size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
