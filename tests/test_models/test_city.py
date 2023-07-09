#!usr/bin/python3
""" Test for city class """
from models.city import City
import unittest


class Test_city(unittest.TestCase):

    def test_class(self):
        new_class = City()
        self.assertTrue(isinstance(new_class, City))
        self.assertIsInstance(new_class, City)
        self.assertTrue(hasattr(new_class, "state_id"))
        self.assertTrue(hasattr(new_class, "name"))
        self.assertEqual(new_class.state_id, "")
        self.assertEqual(new_class.name, "")


if __name__ == '__main__':
    unittest.main()
