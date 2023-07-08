#!/usr/bin/python3
""" Test Filestorage """
import unittest
from os import path
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class Test_File_Storage(unittest.TestCase):
    """ Doc """

    def setUp(self):
        """ check empty """
        try:
            remove('storage.json')
        except Exception:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """ check remove class """
        try:
            remove('storage.json')
        except Exception:
            pass

    def empty_class(self):
        """ empty """

    def test_functios(self):
        """ check  all function """
        storage = FileStorage()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage._FileStorage__objects)

    def test_all(self):
        """ check  all function """
        storage = FileStorage()
        test = storage.all()
        self.assertIsNotNone(test)
        self.assertEqual(type(test), dict)
        self.assertIs(test, storage._FileStorage__objects)

    def test_save_function(self):
        """ Save  """
        test = BaseModel()
        key = 'BaseModel' + '.' + test.id
        test1 = User()
        key_1 = 'User' + '.' + test1.id
        test2 = City()
        key_2 = 'City' + '.' + test2.id
        test3 = Amenity()
        key_3 = 'Amenity' + '.' + test3.id
        test4 = Place()
        key_4 = 'Place' + '.' + test4.id
        test5 = Review()
        key_5 = 'Review' + '.' + test5.id
        test6 = State()
        key_6 = 'State' + '.' + test6.id
        self.assertEqual(test, storage.all()[key])
        self.assertEqual(test1, storage.all()[key_1])
        self.assertEqual(test2, storage.all()[key_2])
        self.assertEqual(test3, storage.all()[key_3])
        self.assertEqual(test4, storage.all()[key_4])
        self.assertEqual(test5, storage.all()[key_5])
        self.assertEqual(test6, storage.all()[key_6])

    def test_reload_function(self):
        """ Reload"""
        test = BaseModel()
        key = 'BaseModel' + '.' + test.id
        test1 = User()
        key_1 = 'User' + '.' + test1.id
        test2 = City()
        key_2 = 'City' + '.' + test2.id
        test3 = Amenity()
        key_3 = 'Amenity' + '.' + test3.id
        test4 = Place()
        key_4 = 'Place' + '.' + test4.id
        test5 = Review()
        key_5 = 'Review' + '.' + test5.id
        test6 = State()
        key_6 = 'State' + '.' + test6.id
        storage.save()
        self.assertTrue(path.isfile('file.json'))
        FileStorage._FileStorage__objects = {}
        storage.reload()
        self.assertTrue(key in storage.all().keys())
        self.assertEqual(test.id, storage.all()[key].id)
        self.assertTrue(key_1 in storage.all().keys())
        self.assertEqual(test1.id, storage.all()[key_1].id)
        self.assertTrue(key_2 in storage.all().keys())
        self.assertEqual(test2.id, storage.all()[key_2].id)
        self.assertTrue(key_3 in storage.all().keys())
        self.assertEqual(test3.id, storage.all()[key_3].id)
        self.assertTrue(key_4 in storage.all().keys())
        self.assertEqual(test4.id, storage.all()[key_4].id)
        self.assertTrue(key_5 in storage.all().keys())
        self.assertEqual(test5.id, storage.all()[key_5].id)
        self.assertTrue(key_6 in storage.all().keys())
        self.assertEqual(test6.id, storage.all()[key_6].id)

    def test_new_classes(self):
        """ check  new method is valid """
        obj = BaseModel(id='123')
        obj_key = 'BaseModel' + '.' + obj.id
        obj1 = User(id='01')
        obj1_key = 'User' + '.' + obj1.id
        obj2 = City(id='02')
        obj2_key = 'City' + '.' + obj2.id
        obj3 = Amenity(id='03')
        obj3_key = 'Amenity' + '.' + obj3.id
        obj4 = Place(id='04')
        obj4_key = 'Place' + '.' + obj4.id
        obj5 = Review(id='05')
        obj5_key = 'Review' + '.' + obj5.id
        obj6 = State(id='06')
        obj6_key = 'State' + '.' + obj6.id

        self.assertEqual(storage.all(), {})
        obj.id = 123
        storage.new(obj)
        storage.new(obj1)
        storage.new(obj2)
        storage.new(obj3)
        storage.new(obj4)
        storage.new(obj5)
        storage.new(obj6)
        self.assertEqual(obj, storage.all()[obj_key])
        self.assertEqual(obj1, storage.all()[obj1_key])
        self.assertEqual(obj2, storage.all()[obj2_key])
        self.assertEqual(obj3, storage.all()[obj3_key])
        self.assertEqual(obj4, storage.all()[obj4_key])
        self.assertEqual(obj5, storage.all()[obj5_key])
        self.assertEqual(obj6, storage.all()[obj6_key])
