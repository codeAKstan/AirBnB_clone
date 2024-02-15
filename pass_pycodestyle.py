#!/usr/bin/python3
""" Pass pycodestyle """
from datetime import datetime
import uuid


class BaseModel:
    """ The base model for other classes """

    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key in {'created_at', 'updated_at'}:
                    setattr(self, key,
                            datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    setattr(self, key, value)

    def __str__(self):
        """ String representation """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ Save method that updates the updated_at """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Returns dictionary representation of instance """
        result_dict = self.__dict__.copy()
        result_dict['__class__'] = self.__class__.__name__
        result_dict['created_at'] = self.created_at.isoformat()
        result_dict['updated_at'] = self.updated_at.isoformat()

        return result_dict
