#!usr/bin/python3
""" Test for review class """
from models.review import Review
import unittest


class Test_review(unittest.TestCase):

    def test_class(self):
        new_class = Review()
        self.assertTrue(isinstance(new_class, Review))
        self.assertIsInstance(new_class, Review)
        self.assertTrue(hasattr(new_class, "place_id"))
        self.assertTrue(hasattr(new_class, "user_id"))
        self.assertTrue(hasattr(new_class, "text"))
        self.assertEqual(new_class.place_id, "")
        self.assertEqual(new_class.user_id, "")
        self.assertEqual(new_class.text, "")


if __name__ == '__main__':
    unittest.main()
