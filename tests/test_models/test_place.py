#!/usr/bin/python3
import unittest
import pep8
import os
from models.place import Place
from models.engine.file_storage import FileStorage


def setUpModule():
    """ Funtion to set a Module"""
    pass


def tearDownModule():
    """ Function to delete a Module"""
    pass


class TestStringMethods(unittest.TestCase):
    """ Check the pep8 """
    def testpep8(self):
        style = pep8.StyleGuide(quiet=True)
        file1 = "models/place.py"
        file2 = "tests/test_models/test_place.py"
        check = style.check_files([file1, file2])
        self.assertEqual(check.total_errors, 0,
                         "Found code style errors (and warning).")


class TestModels(unittest.TestCase):
    """ Funtion to test the BaseModel"""

    def setUp(self):
        """ Set a variable """
        self.place_1 = Place()
        self.place_1.number_bathrooms = 1
        self.place_1.longitude = 10.10
        print("setUp")

    def tearDown(self):
        """ End variable """
        print("tearDown")

    @classmethod
    def setUpClass(cls):
        """ define class """
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        """ close the class """
        print("tearDownClass")

    def test_place_documentation(self):
        """ check documentation """
        self.assertIsNotNone(Place.__doc__)
        self.assertIsNotNone(Place.__init__.__doc__)

    def test_place_city(self):
        """ check if the city name is create """
        self.place_1.save()
        self.assertTrue(os.path.isfile('file.json'))
        self.assertTrue(hasattr(self.place_1, "__init__"))
        self.assertTrue(hasattr(self.place_1, "city_id"))
        self.assertTrue(hasattr(self.place_1, "user_id"))
        self.assertTrue(hasattr(self.place_1, "name"))
        self.assertTrue(hasattr(self.place_1, "description"))
        self.assertTrue(hasattr(self.place_1, "number_rooms"))
        self.assertTrue(hasattr(self.place_1, "number_bathrooms"))
        self.assertTrue(hasattr(self.place_1, "max_guest"))
        self.assertTrue(hasattr(self.place_1, "price_by_night"))
        self.assertTrue(hasattr(self.place_1, "latitude"))
        self.assertTrue(hasattr(self.place_1, "longitude"))
        self.assertTrue(hasattr(self.place_1, "amenity_ids"))

    def test_models_to_dict(self):
        model_1 = self.place_1.to_dict()
        self.assertIsInstance(model_1["created_at"], str)
        self.assertIsInstance(model_1["updated_at"], str)
        self.assertIsInstance(model_1["number_bathrooms"], int)
        self.assertIsInstance(model_1["longitude"], float)
        self.assertIsInstance(model_1["id"], str)

    def test_place_is_instance(self):
        """ check if place_1 is instance of Place """
        self.assertIsInstance(self.place_1, Place)


if __name__ == '__main__':
    unittest.main()