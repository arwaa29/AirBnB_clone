#!/usr/bin/python3
import unittest
import pep8
import os
from models.state import State
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
        file1 = "models/state.py"
        file2 = "tests/test_models/test_state.py"
        check = style.check_files([file1, file2])
        self.assertEqual(check.total_errors, 0,
                         "Found code style errors (and warning).")


class TestModels(unittest.TestCase):
    """ Funtion to test the BaseModel"""

    def setUp(self):
        """ Set a variable """
        self.state_1 = State()
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
        self.assertIsNotNone(State.__doc__)
        self.assertIsNotNone(State.__init__.__doc__)

    def test_place_city(self):
        """ check if the state methods exists """
        self.state_1.save()
        self.assertTrue(os.path.isfile('file.json'))
        self.assertTrue(hasattr(self.state_1, "__init__"))
        self.assertTrue(hasattr(self.state_1, "name"))

    def test_amenity_name(self):
        """ check if the name is create """
        self.state_1.name = 'Good'
        self.assertEqual(self.state_1.name, 'Good')

    def test_models_to_dict(self):
        model_1 = self.state_1.to_dict()
        self.assertIsInstance(model_1["created_at"], str)
        self.assertIsInstance(model_1["updated_at"], str)

    def test_amenity_instance(self):
        """ check if state_1 is instance of State """
        self.assertIsInstance(self.state_1, State)

if __name__ == '__main__':
    unittest.main()