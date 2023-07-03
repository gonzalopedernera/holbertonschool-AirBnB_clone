#!/usr/bin/python3
import uuid

class BaseModel():
    """ Class that defines all common attributes/methods for other classes """
    def __init__(self, id):
        self.id = uuid.uuid4