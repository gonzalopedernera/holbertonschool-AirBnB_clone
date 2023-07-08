#!/usr/bin/python3
""" Module containing class BaseModel """
import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """
    Base class

    Attributes:
        id (str): identifier for the object.
        created_at (datetime): Date and time the object was created.
        updated_at (datetime): Date and time the object was last updated.
    """
    def __init__(self, *args, **kwargs):
        """ comments """

        format = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = str(value)
                if key == 'created_at':
                    self.created_at = datetime.strptime(value, format)
                if key == 'updated_at':
                    self.updated_at = datetime.strptime(value, format)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """ string representation """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ save """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ dictionary representation """

        copy = self.__dict__.copy()
        copy['__class__'] = type(self).__name__
        copy["created_at"] = self.created_at.isoformat()
        copy["updated_at"] = self.updated_at.isoformat()
        return copy
