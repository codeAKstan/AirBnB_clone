#!/usr/bin/python3
""" A class BaseModel that defines all attributes/ methods for other classes
"""

from datetime import datetime
import uuid


class BaseModel:
    """ the base model for other classes """
    def __init__(self, *args, **kwargs):

        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at' or key == 'updated_at':
                    datetime_value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, datetime_value)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()



    def __str__(self):
        """ string representation """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ save method that updates the updated_at """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns dictionary representation of instance """
        result_dict = self.__dict__.copy()
        result_dict['__class__'] = self.__class__.__name__

        result_dict['created_at'] = self.created_at.isoformat()
        result_dict['updated_at'] = self.updated_at.isoformat()

        return result_dict
