#!/usr/bin/python3
""" class FileStorage
    serializes instances to a JSON file
    and deserializes JSON file to instances """
import json
import uuid
import os
from datetime import datetime
from models.base_model import BaseModel


class FileStorage:
    """ construct """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return dictionary objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in dictionary the obj with key <obj class name>.id """
        k = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[k] = obj

    def save(self):
        """ serializes objectss to the JSON file (path: __file_path) """
        dic_object = {}
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as fname:
            for key, val in FileStorage.__objects.items():
                dic_object[key] = val.to_dict()
            json.dump(dic_object, fname)

    def reload(self):
        """ Reload the file """
        try:
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as fname:
                l_json = json.load(fname)
                for key, val in l_json.items():
                    FileStorage.__objects[key] = val(
                        value['__class__'](**value))
        except:
            pass
