#!/usr/bin/python3
"""
this is 'test_file_storage' module

unittest for 'file_storage' module
"""
import unittest
from unittest.mock import MagicMock
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    a class to test FileStorage class and its methods
    """
    def test_class_doctest(self):
        """
        test to check doctest of class
        :return: nth
        """
        self.assertTrue(len(FileStorage.__doc__) > 1)

    def setUp(self):
        """Initializing the unittest
        """
        self.file_storage = FileStorage()

    def tearDown(self):
        """Clean up after the test
        """
        self.file_storage = None

    def test_all(self):
        """Test to check all method
        """
        objects = self.file_storage.all()
        self.assertIsInstance(objects, dict)

    def test_new(self):
        """Test to check new method
        """
        test_model = BaseModel()
        self.file_storage.new(test_model)
        self.assertIn(f"{test_model.__class__.__name__}.{test_model.id}",
                     self.file_storage.all())

    def test_save_reload(self):
        """Test to check save and reload methods
        """
        BaseModel.to_dict = MagicMock(return_value={"key": "value"})

        test_model = BaseModel()
        self.file_storage.new(test_model)
        self.file_storage.save()

        self.file_storage.__objects = {}
        self.file_storage.reload()

        self.assertIn(f"{test_model.__class__.__name__}.{test_model.id}",
                     self.file_storage.all())
        self.assertTrue(BaseModel.to_dict.called)


if __name__ == '__main__':
    unittest.main()
