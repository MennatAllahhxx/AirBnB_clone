#!/usr/bin/python3
""" Module of Unittests """
import unittest
from models.review import Review
from models.base_model import BaseModel
from models import storage
from datetime import datetime


class TestReview(unittest.TestCase):
    """Test cases against the Review class"""

    review = Review()
    review.place_id = "place-123"
    review.user_id = "user-456"
    review.text = "Good place"

    def test_default_values(self):
        """test default value"""

        r = Review()
        self.assertEqual(r.place_id, "")
        self.assertEqual(r.user_id, "")
        self.assertEqual(r.text, "")

    def create_instance_without_kwargs(self):
        """create an instance of class without kwargs"""
        self.assertIsInstance(self.review, Review)
        self.assertIsInstance(self.review, BaseModel)
        self.assertIsInstance(self.review.id, str)
        self.assertIsInstance(self.review.created_at, datetime)
        self.assertIsInstance(self.review.updated_at, datetime)
        self.assertIsInstance(self.review.place_id, str)
        self.assertIsInstance(self.review.user_id, str)
        self.assertIsInstance(self.review.text, str)
        self.assertEqual(self.review.place_id, "place-123")
        self.assertEqual(self.review.user_id, "user-456")
        self.assertEqual(self.review.text, "Good place")

    def create_instance_with_kwargs(self):
        """create an instance of class using kwargs"""
        review_data = {
            "id": "review-789",
            "place_id": "place-456",
            "user_id": "user-789",
            "text": "Beautiful view",
            "created_at": "2023-08-11T23:00:25.886465",
            "updated_at": "2023-08-11T23:00:25.886466"
        }

        new_review = Review(**review_data)

        self.assertIsInstance(new_review, Review)
        self.assertIsInstance(new_review, BaseModel)
        self.assertIsInstance(new_review.id, str)
        self.assertIsInstance(new_review.created_at, datetime)
        self.assertIsInstance(new_review.updated_at, datetime)
        self.assertIsInstance(new_review.place_id, str)
        self.assertIsInstance(new_review.user_id, str)
        self.assertIsInstance(new_review.text, str)

        self.assertEqual(new_review.id, "review-789")
        self.assertEqual(new_review.place_id, "place-456")
        self.assertEqual(new_review.user_id, "user-789")
        self.assertEqual(new_review.text, "Beautiful view")

    def test_to_dict(self):
        """test to_dict method"""
        to_dict_returned_dict = self.review.to_dict()
        expected_dict = self.review.__dict__.copy()
        expected_dict["__class__"] = self.review.__class__.__name__
        expected_dict["updated_at"] = self.review.updated_at.isoformat()
        expected_dict["created_at"] = self.review.created_at.isoformat()
        self.assertDictEqual(expected_dict, to_dict_returned_dict)

    def test_save(self):
        """"test save method"""
        before_update_time = self.review.updated_at
        self.review.text = "Updated review text"
        self.review.save()
        after_update_time = self.review.updated_at
        self.assertNotEqual(before_update_time, after_update_time)

    def test_str(self):
        """test that the str method has the correct output"""
        n = self.review.__class__.__name__
        expected_str = f"[{n}] ({self.review.id}) <{self.review.__dict__}>"
        self.assertEqual(self.review.__str__(), expected_str)


if __name__ == '__main__':
    unittest.main()
