#!usr/bin/python3
""" Test for state class """
from models.state import State
import unittest


class Test_state(unittest.TestCase):

    def test_class(self):
        new_class = State()
        self.assertTrue(isinstance(new_class, State))
        self.assertIsInstance(new_class, State)
        self.assertTrue(hasattr(new_class, "name"))
        self.assertEqual(new_class.name, "")


if __name__ == '__main__':
    unittest.main()
