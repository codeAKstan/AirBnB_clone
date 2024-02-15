#!/usr/bin/python3
""" console.py : contains entry point of the command prompt """
import cmd
import json
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Command interpreter for managing storage"""

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

    def do_create(self, line):
        """Create a new instance of BaseModel or User"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.CLASSES:
            print("** class doesn't exist **")
            return
        new_instance = storage.CLASSES[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """Print the string representation of an instance"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.CLASSES:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        objects = storage.all().get(class_name)
        if objects is None or key not in objects:
            print("** no instance found **")
            return
        print(objects[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.CLASSES:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        objects = storage.all().get(class_name)
        if objects is None or key not in objects:
            print("** no instance found **")
            return
        del objects[key]
        storage.save()

    def do_all(self, line):
        """Prints string representation of all instances"""
        args = line.split()
        objects = storage.all()
        if not args:
            print([str(obj) for obj in objects.values()])
        elif args[0] not in storage.CLASSES:
            print("** class doesn't exist **")
        else:
            class_name = args[0]
            fil_objs = [str(obj)
                        for key, obj in objects.items()
                        if class_name in key]
            print(fil_objs)

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.CLASSES:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        objects = storage.all().get(class_name)
        if objects is None or key not in objects:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return
        attr_val = args[3]
        if attr_val.startswith('"') and attr_val.endswith('"'):
            attr_val = attr_val[1:-1]
        setattr(objects[key], attribute_name, attr_val)
        objects[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
