#!/usr/bin/env python3
""" Airbnb console """

import cmd
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from datetime import datetime, date


class HBNBCommand(cmd.Cmd):
    """ Class to create Airbnb """
    prompt = "(hbnb) "

    classes = ["BaseModel", "User", "State", "Place", "City", "Amenity",
               "Review"]


    def do_quit(self, arg):
        """ Able quit command """
        exit()

    def do_EOF(self, arg):
        """ Able EOF command """
        print('')
        exit()

    def emptyline(self):
        """ Pass enter command """
        pass

    def do_create(self, arg):
        """  Creates a new instance of BaseModel and saves to a JSON file """
        new = None
        if arg:
            new_list = arg.split()
            if len(new_list) == 1:
                if arg in self.dic_class.keys():
                    new = self.dic_class[arg]()
                    new.save()
                    print(new.id)
                else:
                    print("** class doesn't exist **")
        else:
            print('** class name missing **')

    def do_show(self, arg):
        """ Print a representation of instance """
        args = arg.split()
        if not args:
            print('** class name missing **')
            return
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        else:
            try:
                key = args[0] + '.' + args[1]
                print(storage.all[key])
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, arg):
        """ Delete instance by the class name and id """
        args = arg.split()
        if not args:
            print('** class name missing **')
            return
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        else:
            try:
                key = args[0] + '.' + args[1]
                storage.all().pop(key)
                storage.save()
            except KeyError:
                print("** no instance found **")

    def do_all(self, arg):
        """ Prints string representation of instances """
        if not arg:
            my_list = [str(value) for key, value in storage.all().items()]
            if len(my_list) != 0:
                print(my_list)
        elif arg not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            my_list = [str(value) for key,
                       value in storage.all().items() if arg in key]
            if len(my_list) != 0:
                print(my_list)

        def do_update(self, arg):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif (args[0] not in self.classes):
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
            return
        else:
            try:
                key = args[0] + '.' + args[1]
                storage.all()[key]
            except KeyError:
                print('** no instance found **')
                return
            if len(args) == 2:
                print("** attribute name missing **")
                return
            elif len(args) == 3:
                print("** value missing **")
                return
            else:
                key = args[0] + '.' + args[1]
                try:
                    if '.' in args[3]:
                        value = float(args[3])
                    else:
                        value = int(args[3])
                except ValueError:
                    value = str(args[3]).strip("\"':")
                    value = str(value)
                    setattr(storage.all()[key], args[2].strip("\"':"), value)
                    storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
