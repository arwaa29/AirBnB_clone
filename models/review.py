#!/usr/bin/python3
""" class review """
from models.base_model import BaseModel
from models.place import Place
from models.user import User


class Review(BaseModel):
    """ Review class """
    text = ""
    user_id = ""
    place_id = ""

    def __init__(self, *args, **kwargs):
        """ Init """
        super().__init__(*args, **kwargs)