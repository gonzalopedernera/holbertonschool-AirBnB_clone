#!/usr/bin/python3
import json
from os import path

class FileStorage:
    __file_path = "file.json"
    __objetcs = {}

    def all(self):
        return FileStorage.__objetcs
    
    def new(self, obj):

        FileStorage.__objetcs[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):

        dict = {}
        for key, value in FileStorage.__objetcs.items():
            dict.update({key: value.to_dict()})

        with open(FileStorage.__file_path, mode = 'w') as f:
            json.dump(dict, f)

    def reload(self):
        from models.base_model import BaseModel
        if not path.exists(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, mode='r') as f:
            dict = json.load(f)
            classes = {'BaseModel': BaseModel}

            for key, value in dict.items():
                _class = key.split('.')[0]
                if _class in classes.keys():
                    FileStorage.__objetcs[key] = classes[_class](**value)