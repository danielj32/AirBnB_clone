#!/usr/bin/python3
""" Holberton AirBnB Console """
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ General Class for HBNBCommand """
    prompt = '(hbnb) '
    dic_class = {'BaseModel': BaseModel}

    def do_quit(self, arg):
        """ Exit method for quit typing """
        exit()

    def do_EOF(self, arg):
        """ Exit method for EOF """
        print('')
        exit()

    def emptyline(self):
        """ Method to pass when emptyline entered """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
