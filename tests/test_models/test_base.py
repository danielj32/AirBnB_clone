#!/usr/bin/python3
""" testing files """
import unittest
import inspect
import pep8
from models.base_model import BaseModel
from datetime import datetime


class BaseModel_testing(unittest.TestCase):

    def testpep8(self):
        """ testing codestyle """
        pepstylecode = pep8.StyleGuide(quiet=True)
        rest = pepstylecode.check_files(['models/base_model.py',
                                         'models/__init__.py',
                                         'models/engine/file_storage.py'])
        self.assertEqual(rest.total_errors, 0,
                         "Found code style errors (and warnings).")


class test_for_base_model(unittest.TestCase):
    """ Class test for BaseModel """

    def TearDown(self):
        """ delete json file """
        del self.test

    def SetUp(self):
        """ Create instance """
        self.test = BaseModel()

    def test_attr_none(self):
        """None attribute."""
        object_test = BaseModel(None)
        self.assertTrue(hasattr(object_test, "id"))
        self.assertTrue(hasattr(object_test, "created_at"))
        self.assertTrue(hasattr(object_test, "updated_at"))

    def test_kwargs_constructor_2(self):
        """ check id with data """
        dictonary = {'score': 100}

        object_test = BaseModel(**dictonary)
        self.assertTrue(hasattr(object_test, 'id'))
        self.assertTrue(hasattr(object_test, 'created_at'))
        self.assertTrue(hasattr(object_test, 'updated_at'))
        self.assertTrue(hasattr(object_test, 'score'))

    def test_str(self):
        """ Test string """
        dictonary = {'id': 'cc9909cf-a909-9b90-9999-999fd99ca9a9',
                     'created_at': '2025-06-28T14:00:00.000001',
                     '__class__': 'BaseModel',
                     'updated_at': '2030-06-28T14:00:00.000001',
                     'score': 100
                     }

        object_test = BaseModel(**dictonary)
        out = "[{}] ({}) {}\n".format(type(object_test).__name__, object_test.id, object_test.__dict__)

    def test_to_dict(self):
        """ check dict """
        object_test = BaseModel(score=300)
        n_dict = object_test.to_dict()

        self.assertEqual(n_dict['id'], object_test.id)
        self.assertEqual(n_dict['score'], 300)
        self.assertEqual(n_dict['__class__'], 'BaseModel')
        self.assertEqual(n_dict['created_at'], object_test.created_at.isoformat())
        self.assertEqual(n_dict['updated_at'], object_test.updated_at.isoformat())

        self.assertEqual(type(n_dict['created_at']), str)
        self.assertEqual(type(n_dict['created_at']), str)

    def test_datetime(self):
        """ check datatime """
        base1 = BaseModel()
        self.assertFalse(datetime.now() == base1.created_at)
