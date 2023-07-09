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
    classes = {
            "BaseModel": BaseModel,
            "User": User,
            "City": City,
            "State": State,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
            }

    def do_quit(self, arg):
        """Quit command to exit the program

        """
        return True

    def emptyline(self):
        """
        Method to pass when emptyline entered
        """
        pass

    def do_EOF(self, arg):
        """ Quits the program with prompt 'EOF'(ctrl + D)"""
        return True

    def do_help(self, arg):
        """Displays description of a command"""
        cmd.Cmd.do_help(self, arg)

    def do_create(self, arg):
        """Creates a new instance of the class recieved as prompt.
        Saves the changes to the JSON file"""
        if not arg:
            print("** class name missing **")

        elif arg not in HBNBCommand.classes:
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
                return

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
                return
            elif len(arg_list) < 2:
                print("** instance id missing **")
                return

            obj_key = arg_list[0] + '.' + arg_list[1]
            if obj_key in storage.all().keys():
                del (storage.all()[obj_key])
                storage.save()
            else:
                print("** no instance found **")
                return

    def do_all(self, arg):
        """Prints all the instances from the class name recieved as prompt"""
        obj_list = []
        if arg:
            if arg not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return

            else:
                for key, value in storage.all().items():
                    if value.__class__.__name__ == arg:
                        obj_list.append(f"{value}")
                if obj_list != []:
                    print(obj_list)
        else:
            for key, value in storage.all().items():
                obj_list.append(f"{value}")
            if obj_list != []:
                print(obj_list)

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
            return

        else:
            arg_list = args.split()
            if arg_list[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            elif len(arg_list) < 2:
                print("** instance id missing **")
                return
            elif len(arg_list) < 3:
                print("** attribute name missing **")
                return
            elif len(arg_list) < 4:
                print("** value missing **")
                return
            else:
                obj_key = arg_list[0] + "." + arg_list[1]
                all_obj = storage.all()
                if obj_key in all_obj.keys():
                    obj = all_obj[obj_key]
                    if arg_list[3].startswith('"'):
                        obj.__dict__[arg_list[2]] = arg_list[3][1:-1]
                    else:
                        obj.__dict__[arg_list[2]] = arg_list[3]
                    storage.save()
                else:
                    print("** no instance found **")
                    return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
