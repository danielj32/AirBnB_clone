#!/usr/bin/python3
""" User Class """
from models.base_model import BaseModel


class User(BaseModel):
    """ User class that inherits BaseModel """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
