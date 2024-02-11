#!/usr/bin/python3
""" Uniittest for the base model """
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ unittests for basemodel """

    def setUp(self):
        """ Set up a common instance for all test cases """
        self.my_model = BaseModel()

    def test_instance(self):
        """ Test the instance attributes of base model """
        self.assertIsInstance(self.my_model.id, str)
        self.assertIsInstance(self.my_model.created_at, datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime)

    def test_save_method(self):
        """ Test the save method """
        init_time = self.my_model.updated_at
        self.my_model.save()
        self.assertNotEqual(init_time, self.my_model.updated_at)

    def test_to_dict_method(self):
        """ Test the to_dict method """
        result_dict = self.my_model.to_dict()
        self.assertIn('__class__', result_dict)

        self.assertTrue(
            datetime.fromisoformat(result_dict['created_at']) and
            datetime.fromisoformat(result_dict['updated_at']),
            msg="created_at or updated_at is not in ISO format"
        )

    def test_init_with_args_kwargs(self):
        """ Test the __init__ method with *args and **kwargs """
        custom_model = BaseModel(custom_attribute='value')

        self.assertEqual(custom_model.custom_attribute, 'value')

        initial_updated_at = custom_model.updated_at

        dict_representation = custom_model.to_dict()

        recreated_model = BaseModel(**dict_representation)

        self.assertEqual(recreated_model.custom_attribute, 'value')
        self.assertEqual(recreated_model.updated_at, initial_updated_at)


if __name__ == '__main__':
    unittest.main()
