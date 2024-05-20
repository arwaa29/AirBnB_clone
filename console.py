#!/usr/bin/python3
import cmd
import shlex
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

m_class = {"BaseModel": BaseModel, "User": User, "State": State,
            "City": City, "Amenity": Amenity, "Place": Place,
            "Review": Review}


class HBNBCommand(cmd.Cmd):
    """ Command Class """

    prompt = '(hbnb) '
    file = None

    def do_EOF(self, arg):
        'EOF command to exit the program'
        return True

    def do_quit(self, arg):
        'Quit command to exit the program'
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        'Create command to create a new instance'
        if not arg:
            print("** class name missing **")
        elif arg in m_class:
            for key, value in m_class.items():
                if key == arg:
                    new_instance = m_class[key]()
            storage.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        'Show command to show an existing instance.'
        m_arg = arg.split(" ")
        if not arg:
            print("** class name missing **")
        elif m_arg[0] not in m_class:
            print("** class doesn't exist **")
        elif len(m_arg) >= 1:
            try:
                objectss = FileStorage.all(self)
                m_key = m_arg[0] + "." + m_arg[1]
                flag = 0
                for key, values in objectss.items():
                    if key == m_key:
                        flag = 1
                        print(values)
                if flag == 0:
                    print("** no instance found **")
            except IndexError:
                print("** instance id missing **")

    def do_destroy(self, arg):
        'Deletes an instance based on the class name and id'
        m_arg = arg.split(" ")
        if not arg:
            print("** class name missing **")
        elif m_arg[0] not in m_class:
            print("** class doesn't exist **")
        elif len(m_arg) >= 1:
            try:
                objectss = FileStorage.all(self)
                m_key = m_arg[0] + "." + m_arg[1]
                try:
                    objectss.pop(m_key)
                    storage.save()
                except KeyError:
                    print("** no instance found **")
            except IndexError:
                    print("** instance id missing **")

    def do_all(self, arg):
        'Show all instances based on class name.'
        m_arg = arg.split(" ")
        if not arg:
            m_list = []
            objectss = FileStorage.all(self)
            for key, values in objectss.items():
                m_list.append(str(values))
            print(m_list)
        elif m_arg[0] not in m_class:
            print("** class doesn't exist **")
        else:
            m_list = []
            objectss = FileStorage.all(self)
            for key, values in objectss.items():
                m_key = key.split(".")
                if m_key[0] == m_arg[0]:
                    m_list.append(str(values))
            print(m_list)

    def do_update(self, arg):
        'Update the instances based on class name and id.'
        m_arg = shlex.split(arg)
        if len(m_arg) == 0:
            print("** class name missing **")
        elif len(m_arg) == 1:
            print("** instance id missing **")
        elif len(m_arg) == 2:
            print("** attribute name missing **")
        elif len(m_arg) == 3:
            print("** value missing **")
        elif m_arg[0] not in m_class:
            print("** class doesn't exist **")
        else:
            objectss = FileStorage.all(self)
            m_key = m_arg[0] + "." + m_arg[1]
            flag = 0
            for key, values in objectss.items():
                if key == m_key:
                    flag = 1
                    m_values = objectss.get(key)
                    setattr(values, m_arg[2], m_arg[3])
                    values.save()
            if flag == 0:
                print("** no instance found **")

    def do_count(self, arg):
        'Count all instances based on class name.'
        count = 0
        m_arg = arg.split(" ")
        if not arg:
            objectss = FileStorage.all(self)
            for key, values in objectss.items():
                m_list.append(str(values))
            print(m_list)
        elif m_arg[0] not in m_class:
            print("** class doesn't exist **")
        else:
            m_list = []
            objectss = FileStorage.all(self)
            for key, values in objectss.items():
                m_key = key.split(".")
                if m_key[0] == m_arg[0]:
                    count += 1
            print(count)

    def do_BaseModel(self, arg):
        'Send command based on class BaseModel'
        the_class = "BaseModel"
        m_arg = arg.split(".")
        if m_arg[1] == 'all()':
            HBNBCommand.do_all(HBNBCommand, the_class)
        elif m_arg[1] == 'count()':
            HBNBCommand.do_count(HBNBCommand, the_class)
        else:
            prim = m_arg[1].find('("')
            seco = m_arg[1].find('")')
            m_arg1 = m_arg[1][0:prim]
            m_arg2 = m_arg[1][prim + 2: seco]
            if m_arg1 == "show":
                param = the_class + " " + m_arg2
                HBNBCommand.do_show(HBNBCommand, param)
            elif m_arg1 == "destroy":
                param = the_class + " " + m_arg2
                HBNBCommand.do_destroy(HBNBCommand, param)
            else:
                m_arg3 = arg
                m_arg3 = m_arg3.replace('"', ' ')
                m_arg3 = m_arg3.split(',')
                if len(m_arg3) == 0:
                    print("** instance id missing **")
                elif len(m_arg3) == 1:
                    print("** attribute name missing **")
                elif len(m_arg3) == 2:
                    print("** value missing **")
                else:
                    param = ("{} {} {} {}".format(the_class, m_arg3[0][9:],
                             m_arg3[1], m_arg3[2][1:-1]))
                    HBNBCommand.do_update(HBNBCommand, param)

    def do_User(self, arg):
        'Send command based on class User'
        the_class = "User"
        m_arg = arg.split(".")
        if m_arg[1] == 'all()':
            HBNBCommand.do_all(HBNBCommand, the_class)
        elif m_arg[1] == 'count()':
            HBNBCommand.do_count(HBNBCommand, the_class)
        else:
            prim = m_arg[1].find('("')
            seco = m_arg[1].find('")')
            m_arg1 = m_arg[1][0:prim]
            m_arg2 = m_arg[1][prim + 2: seco]
            if m_arg1 == "show":
                param = the_class + " " + m_arg2
                HBNBCommand.do_show(HBNBCommand, param)
            elif m_arg1 == "destroy":
                param = the_class + " " + m_arg2
                HBNBCommand.do_destroy(HBNBCommand, param)
            else:
                m_arg3 = arg
                m_arg3 = m_arg3.replace('"', ' ')
                m_arg3 = m_arg3.split(',')
                if len(m_arg3) == 0:
                    print("** instance id missing **")
                elif len(m_arg3) == 1:
                    print("** attribute name missing **")
                elif len(m_arg3) == 2:
                    print("** value missing **")
                else:
                    param = ("{} {} {} {}".format(the_class, m_arg3[0][9:],
                             m_arg3[1], m_arg3[2][1:-1]))
                    HBNBCommand.do_update(HBNBCommand, param)

    def do_State(self, arg):
        'Send command based on class State'
        the_class = "State"
        m_arg = arg.split(".")
        if m_arg[1] == 'all()':
            HBNBCommand.do_all(HBNBCommand, the_class)
        elif m_arg[1] == 'count()':
            HBNBCommand.do_count(HBNBCommand, the_class)
        else:
            prim = m_arg[1].find('("')
            seco = m_arg[1].find('")')
            m_arg1 = m_arg[1][0:prim]
            m_arg2 = m_arg[1][prim + 2: seco]
            if m_arg1 == "show":
                param = the_class + " " + m_arg2
                HBNBCommand.do_show(HBNBCommand, param)
            elif m_arg1 == "destroy":
                param = the_class + " " + m_arg2
                HBNBCommand.do_destroy(HBNBCommand, param)
            else:
                m_arg3 = arg
                m_arg3 = m_arg3.replace('"', ' ')
                m_arg3 = m_arg3.split(',')
                if len(m_arg3) == 0:
                    print("** instance id missing **")
                elif len(m_arg3) == 1:
                    print("** attribute name missing **")
                elif len(m_arg3) == 2:
                    print("** value missing **")
                else:
                    param = ("{} {} {} {}".format(the_class, m_arg3[0][9:],
                             m_arg3[1], m_arg3[2][1:-1]))
                    HBNBCommand.do_update(HBNBCommand, param)

    def do_City(self, arg):
        'Send command based on class City'
        the_class = "City"
        m_arg = arg.split(".")
        if m_arg[1] == 'all()':
            HBNBCommand.do_all(HBNBCommand, the_class)
        elif m_arg[1] == 'count()':
            HBNBCommand.do_count(HBNBCommand, the_class)
        else:
            prim = m_arg[1].find('("')
            seco = m_arg[1].find('")')
            m_arg1 = m_arg[1][0:prim]
            m_arg2 = m_arg[1][prim + 2: seco]
            if m_arg1 == "show":
                param = the_class + " " + m_arg2
                HBNBCommand.do_show(HBNBCommand, param)
            elif m_arg1 == "destroy":
                param = the_class + " " + m_arg2
                HBNBCommand.do_destroy(HBNBCommand, param)
            else:
                m_arg3 = arg
                m_arg3 = m_arg3.replace('"', ' ')
                m_arg3 = m_arg3.split(',')
                if len(m_arg3) == 0:
                    print("** instance id missing **")
                elif len(m_arg3) == 1:
                    print("** attribute name missing **")
                elif len(m_arg3) == 2:
                    print("** value missing **")
                else:
                    param = ("{} {} {} {}".format(the_class, m_arg3[0][9:],
                             m_arg3[1], m_arg3[2][1:-1]))
                    HBNBCommand.do_update(HBNBCommand, param)

    def do_Amenity(self, arg):
        'Send command based on class Amenity'
        the_class = "Amenity"
        m_arg = arg.split(".")
        if m_arg[1] == 'all()':
            HBNBCommand.do_all(HBNBCommand, the_class)
        elif m_arg[1] == 'count()':
            HBNBCommand.do_count(HBNBCommand, the_class)
        else:
            prim = m_arg[1].find('("')
            seco = m_arg[1].find('")')
            m_arg1 = m_arg[1][0:prim]
            m_arg2 = m_arg[1][prim + 2: seco]
            if m_arg1 == "show":
                param = the_class + " " + m_arg2
                HBNBCommand.do_show(HBNBCommand, param)
            elif m_arg1 == "destroy":
                param = the_class + " " + m_arg2
                HBNBCommand.do_destroy(HBNBCommand, param)
            else:
                m_arg3 = arg
                m_arg3 = m_arg3.replace('"', ' ')
                m_arg3 = m_arg3.split(',')
                if len(m_arg3) == 0:
                    print("** instance id missing **")
                elif len(m_arg3) == 1:
                    print("** attribute name missing **")
                elif len(m_arg3) == 2:
                    print("** value missing **")
                else:
                    param = ("{} {} {} {}".format(the_class, m_arg3[0][9:],
                             m_arg3[1], m_arg3[2][1:-1]))
                    HBNBCommand.do_update(HBNBCommand, param)

    def do_Place(self, arg):
        'Send command based on class Place'
        the_class = "Place"
        m_arg = arg.split(".")
        if m_arg[1] == 'all()':
            HBNBCommand.do_all(HBNBCommand, the_class)
        elif m_arg[1] == 'count()':
            HBNBCommand.do_count(HBNBCommand, the_class)
        else:
            prim = m_arg[1].find('("')
            seco = m_arg[1].find('")')
            m_arg1 = m_arg[1][0:prim]
            m_arg2 = m_arg[1][prim + 2: seco]
            if m_arg1 == "show":
                param = the_class + " " + m_arg2
                HBNBCommand.do_show(HBNBCommand, param)
            elif m_arg1 == "destroy":
                param = the_class + " " + m_arg2
                HBNBCommand.do_destroy(HBNBCommand, param)
            else:
                m_arg3 = arg
                m_arg3 = m_arg3.replace('"', ' ')
                m_arg3 = m_arg3.split(',')
                if len(m_arg3) == 0:
                    print("** instance id missing **")
                elif len(m_arg3) == 1:
                    print("** attribute name missing **")
                elif len(m_arg3) == 2:
                    print("** value missing **")
                else:
                    param = ("{} {} {} {}".format(the_class, m_arg3[0][9:],
                             m_arg3[1], m_arg3[2][1:-1]))
                    HBNBCommand.do_update(HBNBCommand, param)

    def do_Review(self, arg):
        'Send command based on class Review'
        the_class = "Review"
        m_arg = arg.split(".")
        if m_arg[1] == 'all()':
            HBNBCommand.do_all(HBNBCommand, the_class)
        elif m_arg[1] == 'count()':
            HBNBCommand.do_count(HBNBCommand, the_class)
        else:
            prim = m_arg[1].find('("')
            seco = m_arg[1].find('")')
            m_arg1 = m_arg[1][0:prim]
            m_arg2 = m_arg[1][prim + 2: seco]
            if m_arg1 == "show":
                param = the_class + " " + m_arg2
                HBNBCommand.do_show(HBNBCommand, param)
            elif m_arg1 == "destroy":
                param = the_class + " " + m_arg2
                HBNBCommand.do_destroy(HBNBCommand, param)
            else:
                m_arg3 = arg
                m_arg3 = m_arg3.replace('"', ' ')
                m_arg3 = m_arg3.split(',')
                if len(m_arg3) == 0:
                    print("** instance id missing **")
                elif len(m_arg3) == 1:
                    print("** attribute name missing **")
                elif len(m_arg3) == 2:
                    print("** value missing **")
                else:
                    param = ("{} {} {} {}".format(the_class, m_arg3[0][9:],
                             m_arg3[1], m_arg3[2][1:-1]))
                    HBNBCommand.do_update(HBNBCommand, param)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
