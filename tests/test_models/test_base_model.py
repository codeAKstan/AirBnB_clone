#!/usr/bin/python3
""" Uniittest for the base model """
import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """ unittests for basemodel """

    def test_instance(self):
        """ test the instance attributes of base model """
        my_model = BaseModel()

        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_save_method(self):
        """ test the save method """
        my_model = BaseModel()

        init_time = my_model.updated_at
        my_model.save()

        self.assertNotEqual(init_time, my_model.updated_at)

    def test_to_dict_method(self):
        """ Test the to_dict method """
        my_model = BaseModel()
        result_dict = my_model.to_dict()

        self.assertIn('__class__', result_dict)

        """ check if created_at and updated_at are in iso format """

        self.assertTrue(
            datetime.fromisoformat(result_dict['created_at']),
            msg="created_at is not in ISO format")
        self.assertTrue(
            datetime.fromisoformat(result_dict['updated_at']),
            msg="updated_at is not in ISO format")


if __name__ == '__main__':
    unittest.main()
