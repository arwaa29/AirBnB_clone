#!/usr/bin/python3
""" class amenity """
from models.base_model import BaseModel

class Amenity(BaseModel):
    """ Amenity class """
    name = ""

    def __init__(self, *args, **kwargs):
        """ Init """
        super().__init__(*args, **kwargs)
