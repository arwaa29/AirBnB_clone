#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new User --")
n_user = User()
n_user.first_name = "Betty"
n_user.last_name = "Holberton"
n_user.email = "airbnb@holbertonshool.com"
n_user.password = "root"
n_user.save()
print(n_user)

print("-- Create a new User 2 --")
n_user2 = User()
n_user2.first_name = "John"
n_user2.email = "airbnb2@holbertonshool.com"
n_user2.password = "root"
n_user2.save()
print(n_user2)