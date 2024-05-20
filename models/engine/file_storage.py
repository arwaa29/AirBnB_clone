
#!usr/bin/python3
""" class file_storage """
import json
from ..base_model import BaseModel
from ..user import User
from ..place import Place
from ..state import State
from ..city import City
from ..amenity import Amenity
from ..review import Review


class FileStorage:
    """ Clase file Storage"""

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """ Init """
        pass

    def all(self):
        """ return __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Create a new instance """
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__,
                                             obj.id)] = obj

    def save(self):
        """ Save function """
        my_dict = {}
        for key, value in FileStorage.__objects.items():
            my_dict.update({key: value.to_dict()})
        js_file = json.dumps(my_dict)
        with open(FileStorage.__file_path, "w") as f:
            f.write(js_file)

    def reload(self):
        """ Reload from JSON file """
        my_dict = {"BaseModel": BaseModel, "User": User, "State": State,
                   "City": City, "Amenity": Amenity, "Place": Place,
                   "Review": Review}

        js_file = ""
        try:
            with open(FileStorage.__file_path, "r") as f:
                js_file = json.loads(f.read())
                for key in js_file:
                    FileStorage.__objects[key] = my_dict[js_file[key]['__class__']](**js_file[key])
        except:
            pass
