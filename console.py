#!/usr/bin/python3
"""Import modules cmd and BaseModel class"""
import cmd
from models.base_model import BaseModel
from models import storage
"""Console for AirBnB clone"""


class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '
    file = None
    classes = {"BaseModel" : BaseModel}
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
            FileStorage.new(obj)
            print("{}".format(obj.id))

    def do_show(self, args):
        """Shows the object with the id recieved as prompt"""
        if not args:
            print("** class name missing **")
        else:
            arg_list = args.split()
            if arg_list[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")

            elif len(arg_list) < 2:
                print("** instance id missing **")
            
            obj_key = arg_list[0] + "." + arg_list[1]
            if obj_key in FileStorage.__objects.keys():
                print(f"FileStorage.__objects[obj_key]")
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
            


    def do_all(self, arg):
        """Prints all the instances from the class name recieved as prompt"""
        if arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            for key, value in FileStorage.__objects.items():
                print(f"value", end="")
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
                if obj_key in FileStorage.__objects.keys():
                    obj = FileStorage.__objects[obj_key]
                    obj.arg_list[2] = arg_list[3]
                    FileStorage.save()
                else:
                    print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()