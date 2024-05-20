#!/usr/bin/python3
import unittest
import pep8
import os
from models.amenity import Amenity
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
        file1 = "models/amenity.py"
        file2 = "tests/test_models/test_amenity.py"
        check = style.check_files([file1, file2])
        self.assertEqual(check.total_errors, 0,
                         "Found code style errors (and warning).")


class TestModels(unittest.TestCase):
    """ Funtion to test the BaseModel"""

    def setUp(self):
        """ Set a variable """
        self.amenity_1 = Amenity()
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

    def test_amenity_doc(self):
        """ Check the documentation """
        self.assertIsNotNone(Amenity.__doc__)
        self.assertIsNotNone(Amenity.__init__.__doc__)

    def test_place_city(self):
        """ check if the amenity methods exists """
        self.amenity_1.save()
        self.assertTrue(os.path.isfile('file.json'))
        self.assertTrue(hasattr(self.amenity_1, "__init__"))
        self.assertTrue(hasattr(self.amenity_1, "name"))

    def test_amenity_name(self):
        """ check if the name is create """
        self.amenity_1.name = 'Good'
        self.assertEqual(self.amenity_1.name, 'Good')

    def test_models_to_dict(self):
        model_1 = self.amenity_1.to_dict()
        self.assertIsInstance(model_1["created_at"], str)
        self.assertIsInstance(model_1["updated_at"], str)
        self.assertIsInstance(model_1["id"], str)

    def test_amenity_instance(self):
        """ check if amenity_1 is instance of Amenity """
        self.assertIsInstance(self.amenity_1, Amenity)

if __name__ == '__main__':
    unittest.main()