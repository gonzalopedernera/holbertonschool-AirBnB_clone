#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel():
    """ Class that defines all common attributes/methods for other classes """
    def __init__(self):
        self.created_at = datetime.now()
        self.id = str(uuid.uuid4())
        self.updated_at = datetime.now()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        update = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        create = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        copy = self.__dict__.copy()
        copy['class'] = type(self).__name__
        copy["update_at"] = self.updated_at.isoformat()
        copy["created_at"] = self.created_at.isoformat()
        return copy
