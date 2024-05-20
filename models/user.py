#!/usr/bin/python3
""" class user """
from models.base_model import BaseModel


class User(BaseModel):
    """ User class """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """ Init """
        super().__init__(*args, **kwargs)