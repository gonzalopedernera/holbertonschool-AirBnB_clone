#!/usr/bin/python3
"""Import modules cmd and BaseModel class"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models import storage
from models.amenity import Amenity
from models.review import Review
from models.place import Place
"""Console for AirBnB clone"""


class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '
    file = None
    classes = {"BaseModel" : BaseModel, "User" : User, "City" : City, "State" : State, "Amenity" : Amenity, "Place" : Place, "Review" : Review}

    def do_quit(self, arg):
        """Quits the program with prompt 'quit'"""
        return True

    def help_quit(self):
        """Help string for do_quit method"""
        print("Quit command to exit the program\n")

    def do_EOF(self, arg):
        """Quits the program with prompt 'EOF'(ctrl + D)"""
        return True

    def help_EOF(self):
        """Help string for do_EOF method"""
        print("EOF command to exit the program\n")

    def do_help(self, arg):
        """Prints a help string for each command with prompt 'help'.
        If help + <command>, the method help_<command> executes
        Otherwise, a list of possible commands is displayed"""
        cmd.Cmd.do_help(self, arg)

    def help_help(self):
        """Help string for do_help method"""
        print("Help command to get help about other commands\n")

    def do_create(self, arg):
        """Creates a new instance of the class recieved as prompt.
        Saves the changes to the JSON file"""
        if arg is None:
            print("** class name missing **")

        if arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            obj = HBNBCommand.classes[arg]()
            storage.new(obj)
            storage.save()
            print("{}".format(obj.id))

    def do_show(self, args):
        """Shows the object with the id recieved as prompt"""
        if not args:
            print("** class name missing **")
        else:
            arg_list = args.split()
            if arg_list[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return

            elif len(arg_list) < 2:
                print("** instance id missing **")
                return

            obj_key = arg_list[0] + "." + arg_list[1]
            if obj_key in storage.all().keys():
                print(f"{storage.all()[obj_key]}")
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """Recieves a class name and an object id as prompt.
        Deleted the object with that id in that class.
        Saves all changes to the JSON file"""
        if not args:
            print("** class name missing **")
        else:
            arg_list = args.split()
            if arg_list[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            elif len(arg_list) < 2:
                print("** instance id missing **")
            obj_key = arg_list[0] + '.' + arg_list[1]
            if obj_key in storage.all().keys():
                del(storage.all()[obj_key])
            else:
                print("** no instance found **")
            



    def do_all(self, arg):
        """Prints all the instances from the class name recieved as prompt"""
        if arg:
            if arg not in HBNBCommand.classes:
                print("** class doesn't exist **")
            else:
                for key, value in storage.all().items():
                    if value.__class__.__name__ == arg:
                        print(f"{value}", end="")
                print()
        else:
            for key, value in storage.all().items():
                print(f"{value}", end="")
            print()

    def do_update(self, args):
        """Updates an object and saves the changes to the JSON file
        Expected prompts (in order):
            class name
            object id
            attribute name
            attribute value
        """
        if not args:
            print("** class name missing **")
        else:
            arg_list = args.split()
            if arg_list[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
            elif len(arg_list) < 2:
                print("** instance id missing **")
            elif len(arg_list) < 3:
                print("** attribute name missing **")
            elif len(arg_list) < 4:
                print("** value missing **")
            else:
                obj_key = arg_list[0] + "." + arg_list[1]
                all_obj = storage.all()
                if obj_key in all_obj.keys():
                    obj = all_obj[obj_key]
                    obj.__dict__[arg_list[2]] = arg_list[3]
                    storage.save()
                else:
                    print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()