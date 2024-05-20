#!/usr/bin/python3
""" class city """
from models.base_model import BaseModel
from models.state import State


class City(BaseModel):
    """ City class """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """ Init """
        super().__init__(*args, **kwargs)