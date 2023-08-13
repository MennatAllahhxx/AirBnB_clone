#!/usr/bin/python3
"""Our BaseModel that defines all common attributes/methods for other classes
"""
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:

    """BaseModel class."""

    def __init__(self, *args, **kwargs):
        """Instance Constructor.
        """
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for k, v in kwargs.items():
                if k != "__class__":
                    if k == "updated_at":
                        self.updated_at = datetime.fromisoformat(v)
                    elif k == "created_at":
                        self.created_at = datetime.fromisoformat(v)
                    else:
                        setattr(self, k, v)

    def __str__(self):
        """return string Representation.
        """
        return f"[{self.__class__.__name__}] ({self.id}) <{self.__dict__}>"

    def save(self):
        """Updates the public instance attribute updated_at
        with the current date and time"""

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values \
        of __dict__ of the instance"""

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict["created_at"] = self.created_at.isoformat()
        return my_dict
