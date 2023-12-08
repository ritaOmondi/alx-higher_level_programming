#!/usr/bin/python3
"""Defines Base class"""
import json
import csv
import turtle


class Base:
    """Base class body.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the  Id in a constructor
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
