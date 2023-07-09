#!usr/bin/python3
""" Test for place class """
from models.place import Place
import unittest


class Test_place(unittest.TestCase):

    def test_class(self):
        new_class = Place()
        self.assertTrue(isinstance(new_class, Place))
        self.assertIsInstance(new_class, Place)
        self.assertTrue(hasattr(new_class, "city_id"))
        self.assertTrue(hasattr(new_class, "user_id"))
        self.assertTrue(hasattr(new_class, "name"))
        self.assertTrue(hasattr(new_class, "description"))
        self.assertTrue(hasattr(new_class, "number_rooms"))
        self.assertTrue(hasattr(new_class, "number_bathrooms"))
        self.assertTrue(hasattr(new_class, "max_guest"))
        self.assertTrue(hasattr(new_class, "price_by_night"))
        self.assertTrue(hasattr(new_class, "latitude"))
        self.assertTrue(hasattr(new_class, "longitude"))
        self.assertTrue(hasattr(new_class, "amenity_ids"))
        self.assertEqual(new_class.city_id, "")
        self.assertEqual(new_class.user_id, "")
        self.assertEqual(new_class.name, "")
        self.assertEqual(new_class.description, "")
        self.assertEqual(new_class.number_rooms, 0)
        self.assertEqual(new_class.number_bathrooms, 0)
        self.assertEqual(new_class.max_guest, 0)
        self.assertEqual(new_class.price_by_night, 0)
        self.assertEqual(new_class.latitude, 0.0)
        self.assertEqual(new_class.longitude, 0.0)
        self.assertEqual(new_class.amenity_ids, [])


if __name__ == '__main__':
    unittest.main()
