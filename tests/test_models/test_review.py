#!/usr/bin/python3
import unittest
import pep8
import os
from models.review import Review
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
        file1 = "models/review.py"
        file2 = "tests/test_models/test_review.py"
        check = style.check_files([file1, file2])
        self.assertEqual(check.total_errors, 0,
                         "Found code style errors (and warning).")


class TestModels(unittest.TestCase):
    """ Funtion to test the BaseModel"""

    def setUp(self):
        """ Set a variable """
        self.review_1 = Review()
        self.review_1.user_id = "asd123"
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

    def test_user_doc(self):
        self.assertIsNotNone(Review.__doc__)
        self.assertIsNotNone(Review.__init__.__doc__)

    def test_review_exist(self):
        """ check if the methods exists """
        self.review_1.save()
        self.assertTrue(os.path.isfile('file.json'))
        self.assertTrue(hasattr(self.review_1, "__init__"))
        self.assertTrue(hasattr(self.review_1, "text"))
        self.assertTrue(hasattr(self.review_1, "user_id"))
        self.assertTrue(hasattr(self.review_1, "place_id"))

    def test_models_to_dict(self):
        model_1 = self.review_1.to_dict()
        self.assertIsInstance(model_1["created_at"], str)
        self.assertIsInstance(model_1["updated_at"], str)
        self.assertIsInstance(model_1["user_id"], str)
        self.assertIsInstance(model_1["id"], str)

    def test_user_instance(self):
        """ check if review_1 is instance of Review """
        self.assertIsInstance(self.review_1, Review)

if __name__ == '__main__':
    unittest.main()