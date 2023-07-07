#!/usr/bin/python3
""" Module containing class BaseModel """
import uuid
from datetime import datetime


class BaseModel():
    """
    Base class for all other classes

    Attributes:
        id (str): Unique identifier for the object.
        created_at (datetime): Date and time the object was created.
        updated_at (datetime): Date and time the object was last updated.
    """
    def __init__(self, *args, **kwargs):
        format = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = str(value)
                if key == 'created_at':
                    self.created_at = datetime.strptime(value, format)
                if key == 'update_at':
                    self.updated_at = datetime.strptime(value, format)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        copy = self.__dict__.copy()
        copy['class'] = type(self).__name__
        copy["created_at"] = self.created_at.isoformat()
        copy["update_at"] = self.updated_at.isoformat()
        return copy
