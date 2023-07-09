#!usr/bin/python3
""" Test for user class """
from models.user import User
import unittest


class Test_user(unittest.TestCase):

    def test_class(self):
        new_class = User()
        self.assertTrue(isinstance(new_class, User))
        self.assertIsInstance(new_class, User)
        self.assertTrue(hasattr(new_class, "email"))
        self.assertTrue(hasattr(new_class, "password"))
        self.assertTrue(hasattr(new_class, "first_name"))
        self.assertTrue(hasattr(new_class, "last_name"))
        self.assertEqual(new_class.email, "")
        self.assertEqual(new_class.password, "")
        self.assertEqual(new_class.first_name, "")
        self.assertEqual(new_class.last_name, "")


if __name__ == '__main__':
    unittest.main()
