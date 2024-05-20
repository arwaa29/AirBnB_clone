#!/user/bin/python3
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """ BaseModel for AirBnB project """
    def __init__(self, *args, **kwargs):
        """ Init method """
        if len(kwargs) is not 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = kwargs[key]
                if key == "created_at":
                    self.created_at = datetime.strptime(kwargs[key],
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                if key == "updated_at":
                    self.updated_at = datetime.strptime(kwargs[key],
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                if key == "my_number":
                    self.my_number = kwargs[key]
                if key == "name":
                    self.name = kwargs[key]
        else:
            self.id:str = str(uuid4())
            self.created_at:datetime= datetime.now()
            self.updated_at:datetime = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ for print """
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """ updates the update_at """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self)->dict:
        """ Returns a dictionary """
        my_dict :dict = self.__dict__.copy()
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict['__class__'] = self.__class__.__name__
        return(my_dict)