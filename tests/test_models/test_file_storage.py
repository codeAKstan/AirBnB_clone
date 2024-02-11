#!/usr/bin/python3
""" unittest for file storage """
import unittest
import os
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """ test file storage """
    def setUp(self):
        """ setup for all the test cases """
        self.file_path = "test_file.json"
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = self.file_path
        self.obj = BaseModel()

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        obj_dict = self.storage.all()
        self.assertIsInstance(obj_dict, dict)

    def test_new(self):
        self.storage.new(self.obj)
        obj_dict = self.storage.all()
        key = "BaseModel." + self.obj.id
        self.assertIn(key, obj_dict)
        self.assertEqual(obj_dict[key], self.obj)

    def test_save_reload(self):
        self.storage.new(self.obj)
        self.storage.save()
        new_storage = FileStorage()
        new_storage._FileStorage__file_path = self.file_path
        new_storage.reload()
        obj_dict = new_storage.all()
        key = "BaseModel." + self.obj.id
        self.assertIn(key, obj_dict)
        reloaded_obj = obj_dict[key]
        self.assertEqual(reloaded_obj.id, self.obj.id)
        self.assertEqual(reloaded_obj.created_at, self.obj.created_at)
        self.assertEqual(reloaded_obj.updated_at, self.obj.updated_at)


if __name__ == '__main__':
    unittest.main()
