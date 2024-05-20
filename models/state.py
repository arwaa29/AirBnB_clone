#!/usr/bin/python3
""" class user """
from models.base_model import BaseModel


class State(BaseModel):
    """ State class """
    name = ""

    def __init__(self, *args, **kwargs):
        """ Init """
        super().__init__(*args, **kwargs)