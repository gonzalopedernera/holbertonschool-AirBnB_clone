#!/usr/bin/python3
""" class city """
from models.base_model import BaseModel
from models.state import State


class City(BaseModel):
    """ class City """

    state_id = ""
    name = ""
