#!/usr/bin/python3
""" Check Filestorage class """
import unittest
from datetime import datetime
from models.engine import file_storage
from models.base_model import BaseModel

FileStorage = file_storage.FileStorage
clas_dict = {}


class TestFileStorage(unittest.TestCase):
    """Testing the FileStorage class"""
    def test_all_returns_dict(self):
        """check  all returns attr"""
        storage = FileStorage()
        n_dict = storage.all()
        self.assertEqual(type(n_dict), dict)
        self.assertIs(n_dict, storage._FileStorage__objects)

    def test_new(self):
        """check  attr"""
        storage = FileStorage()
        storage._FileStorage__objects = {}
        n_dict = {}
        for key, value in clas_dict.items():
            with self.subTest(key=key, value=value):
                instance = value()
                instance_key = instance.__class__.__name__ + "." + instance.id
                storage.new(instance)
                n_dict[instance_key] = instance
                self.assertEqual(n_dict, storage._FileStorage__objects)
        storage._FileStorage__objects = {}
