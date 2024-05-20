#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
m_model = BaseModel()
m_model.name = "Holberton Medellin COLOMBIA"
m_model.m_number = 5261
m_model.save()
print(m_model)