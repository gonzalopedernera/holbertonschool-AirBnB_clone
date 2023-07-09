# usr/bin/python3
""" unittest for Class BaseModel """
import unittest
import io
from datetime import datetime
from unittest.mock import patch
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from contextlib import redirect_stdout
import os


class Test_BaseModel(unittest.TestCase):

    base = BaseModel()

    def setUp(self):
        self.base = BaseModel()

    def setUp(self):
        """ Test file saving"""
        with open("file.json", "w") as f:
            FileStorage.__file_path = 'file.json'
            FileStorage.__objects = {}

    def tearDown(self):
        """ Destroys created file"""
        try:
            os.remove(FileStorage.__file_path)
        except FileNotFoundError:
            pass

    def test_inst(self):
        """check class """
        ml = BaseModel()
        self.assertTrue(ml, BaseModel)

    def test_actual_time(self):
        my_model = BaseModel()
        my_model.save()
        time = datetime.now()
        self.assertFalse(my_model.updated_at == time)

    def test_save(self):
        self.base = BaseModel()
        old_updated_at = self.base.updated_at
        self.base.save()
        self.assertNotEqual(old_updated_at, self.base.updated_at)

    def test_attr_none(self):
        """None attribute."""
        test = BaseModel(None)
        self.assertTrue(hasattr(test, "id"))
        self.assertTrue(hasattr(test, "created_at"))
        self.assertTrue(hasattr(test, "updated_at"))

    def test_to_dict(self):
        diccionary = BaseModel()
        dict = diccionary.to_dict()
        self.assertEqual(dict['id'], diccionary.id)
        self.assertEqual(dict['created_at'], diccionary.created_at.isoformat())
        self.assertEqual(dict['updated_at'], diccionary.updated_at.isoformat())
        self.assertEqual(dict['__class__'], 'BaseModel')


    def test_str(self):
        """Test of BaseModel __str__ method."""
        self.assertEqual(Test_BaseModel.base.__str__(),
                         f'[{Test_BaseModel.base.__class__.__name__}] '
                         f'({Test_BaseModel.base.id}) {Test_BaseModel.base.__dict__}')

    def test_save2(self):
        """Check what save does"""
        with self.assertRaises(AttributeError):
            BaseModel.save(["Hello, World"])
            BaseModel.save([111, 111, 111, 111])

    def test_save3(self):
        """ Test save method """
        base = BaseModel()
        base.save()
        with open("file.json", "r") as f:
            self.assertIn("BaseModel." + base.id, f.read())

    def test_thetime(self):
        """ test the actual datetime """
        test = BaseModel()
        test.save()
        time = datetime.now()
        self.assertFalse(test == time)
