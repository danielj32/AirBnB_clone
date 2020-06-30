#!/usr/bin/python3
""" testing files """
import unittest
import inspect
import pep8
from models.base_model import BaseModel

class BaseModel_testing(unittest.TestCase):

    def testpep8(self):
        """ testing codestyle """
        pepstylecode = pep8.StyleGuide(quiet=True)
        rest = pepstylecode.check_files(['models/base_model.py'])
        self.assertEqual(rest.total_errors, 0,
                        "Found code style errors (and warnings).")
