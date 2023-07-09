#!/usr/bin/python3
""" Module containing class FileStorage """
import json
from os import path


class FileStorage:
    """
    Serialize instances to a JSON file
    and deserialize JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):

        instances = {}
        for key, value in self.__objects.items():
            instances.update({key: value.to_dict()})

        with open(FileStorage.__file_path, mode='w') as f:
            json.dump(instances, f)

    def reload(self):
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        if not path.exists(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, mode='r') as f:
            instances = json.load(f)
            classes = {'BaseModel': BaseModel, 'User': User, 'State': State,
                       'City': City, 'Amenity': Amenity,
                       'Place': Place, 'Review': Review}

            for key, value in instances.items():
                _class = key.split('.')[0]
                if _class in classes.keys():
                    self.__objects[key] = classes[_class](**value)
