#!/usr/bin/python3
""" console.py : contains entry point of the command prompt """
import cmd


class HBNBCommand(cmd.Cmd):
    """ command interpreter """
    prompt = "(hbnb)"

    def do_quit(self, line):
        """Quit command to exit the program """
        return True

    def do_EOF(self, line):
        """EOF command to exit the program """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
