#!/usr/bin/python3
""" console.py : contains entry point of the command prompt """
import cmd


class HBNBCommand(cmd.Cmd):
    """ command interpreter """
    prompt = '(hbnb) '

    def emptyline(self):
        """Do nothing for emptyline"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        print("")
        return True


if _name_ == '_main_':
    HBNBCommand().cmdloop()
