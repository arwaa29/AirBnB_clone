#!/usr/bin/python3
import unittest
import pep8
import os
from models.city import City
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
        file1 = "models/city.py"
        file2 = "tests/test_models/test_city.py"
        check = style.check_files([file1, file2])
        self.assertEqual(check.total_errors, 0,
                         "Found code style errors (and warning).")


class TestModels(unittest.TestCase):
    """ Funtion to test the BaseModel"""

    def setUp(self):
        """ Set a variable """
        self.city_1 = City()
        self.city_1.state_id = "100"
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

    def test_city_doc(self):
        """ Check the documentation """
        self.assertIsNotNone(City.__doc__)
        self.assertIsNotNone(City.__init__.__doc__)

    def test_city_exist(self):
        """ check if the city methos exists """
        self.city_1.save()
        self.assertTrue(os.path.isfile('file.json'))
        self.assertTrue(hasattr(self.city_1, "__init__"))
        self.assertTrue(hasattr(self.city_1, "state_id"))
        self.assertTrue(hasattr(self.city_1, "name"))

    def test_city_name(self):
        """ check if the name is create """
        self.city_1.name = 'Paris'
        self.assertEqual(self.city_1.name, 'Paris')

    def test_models_to_dict(self):
        model_1 = self.city_1.to_dict()
        self.assertIsInstance(model_1["created_at"], str)
        self.assertIsInstance(model_1["updated_at"], str)
        self.assertIsInstance(model_1["state_id"], str)
        self.assertIsInstance(model_1["id"], str)

    def test_city_instance(self):
        """ check if city_1 is instance of City """
        self.assertIsInstance(self.city_1, City)

if __name__ == '__main__':
    unittest.main()