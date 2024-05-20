#!/usr/bin/python3
from models.base_model import BaseModel

m_model = BaseModel()
m_model.name = "Holberton"
m_model.m_number = 89
print(m_model)
m_model.save()
print(m_model)
m_model_json = m_model.to_dict()
print(m_model_json)
print("JSON of m_model:")
for key in m_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(m_model_json[key]), m_model_json[key]))