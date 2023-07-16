#!/usr/bin/python3
"""
This module contains unittests for Base Class, Rectangle, and Square classes
from the 'models' package. 

The TestBaseClass provides multiple unit tests to ensure correct behavior 
of the various methods and variables in these classes. This includes
tests for standard output, presence of docstrings, instantiation of classes, 
correct incrementing of id, presence of methods in the base class,
error handling, JSON serialization, object creation, and file loading.

This script is executable and runs the tests upon execution.
"""

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest, sys, json
from unittest.mock import patch
from io import StringIO
import os


class TestBaseClass(unittest.TestCase):
    """test Class base"""

    @classmethod
    def setUpClass(cls):
        """methode class setup"""

        cls.bs1 = Base()
        cls.bs2 = Base(100)
        cls.bs3 = Base()
        cls.rt1 = Rectangle(10, 10)
        cls.rt2 = Rectangle(20, 20, id=1000)
        cls.rt3 = Rectangle(30, 30, 3, 3, id=100)
        cls.sq1 = Square(10)
        cls.sq2 = Square(5, 5, 4, id=200)
        cls.sq3 = Square(12, id=22)

    @classmethod
    def tearDownClass(cls):
        """all test object cleared"""
        del cls.bs1
        del cls.bs2
        del cls.bs3

    def test_output(self):
        """stdout test"""
        school = "Coding"
        language = "Python3"
        testing = "Unittest"
        expected_output = "{} {} {}".format(school, language, testing)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            print("Coding Python3 Unittest")
            self.assertEqual(fake_out.getvalue().strip(), expected_output)

    def test_base_cls_doc(self):
        """check docstring is present for class"""
        self.assertIsNotNone(Base.__doc__)

    def test_base_instance_doc(self):
        """instance base if is present"""
        self.assertIsNotNone(self.sq1.__doc__)
        self.assertIsNotNone(self.rt1.__doc__)
        self.assertIsNotNone(self.sq1.__doc__)

    def test_base_methods_doc(self):
        """all methode docsring presents"""
        self.assertTrue(Base.__init__.__doc__)
        self.assertTrue(Base.integer_validator.__doc__)
        self.assertTrue(Base.integer_validator2.__doc__)
        self.assertTrue(Base.to_json_string.__doc__)
        self.assertTrue(Base.from_json_string.__doc__)
        self.assertTrue(Base.save_to_file.__doc__)
        self.assertTrue(Base.create.__doc__)
        self.assertTrue(Base.load_from_file.__doc__)

    def test_class_var_exist(self):
        """is class variable value is  after instantiation"""
        self.assertIsNotNone(Base._Base__nb_objects)

    def test_base_init_id(self):
        """test initiation test"""
        self.assertEqual(self.bs1.id, 1)
        self.assertEqual(self.bs2.id, 100)
        self.assertEqual(self.bs3.id, 2)

    def test_obj_id_exist(self):
        """obj id is incrementing correctly checked"""
        self.assertIsNotNone(self.bs1.id)
        self.assertIsNotNone(Base._Base__nb_objects)

    def test_clsVar_match_id(self):
        """var to obj id match"""
        self.assertEqual(Base._Base__nb_objects, self.sq1.id)

    def test_obj_id(self):
        """if id is assigning"""
        self.assertEqual(self.rt2.id, 1000)
        self.assertEqual(self.sq2.id, 200)
        self.assertEqual(self.sq3.id, 22)
        self.assertEqual(self.bs1.id, 1)

    def test_base_methods(self):
        """method exists on base"""
        self.assertTrue(hasattr(Base, "__init__"))
        self.assertTrue(hasattr(Base, "integer_validator"))
        self.assertTrue(hasattr(Base, "integer_validator2"))
        self.assertTrue(hasattr(Base, "to_json_string"))
        self.assertTrue(hasattr(Base, "from_json_string"))
        self.assertTrue(hasattr(Base, "save_to_file"))
        self.assertTrue(hasattr(Base, "create"))
        self.assertTrue(hasattr(Base, "load_from_file"))

    def test_int_value(self):
        """correct value error rising"""
        with self.assertRaises(ValueError):
            self.rt1.integer_validator(-20, -20)

    def test_int_type(self):
        """correct type error rising"""
        with self.assertRaises(TypeError):
            self.rt2.integer_validator2("str", "str")

    def test_to_json(self):
        """save list to json tested"""
        list1 = [
            {'id': 100},
            {'height': 88},
            {'width': 1, 'id': 2, 'height': 88},
            {'id': 4, 'height': 144, 'weight': 700},
            {'width': 22, 'height': 11}
        ]
        empty = []

        rect_to_json = Rectangle.to_json_string(list1)
        base_to_json = Base.to_json_string(list1)

        rect_to_empty_json = Rectangle.to_json_string(empty)
        base_to_empty_json = Base.to_json_string(empty)

        self.assertIsInstance(list1, list)
        self.assertIsInstance(rect_to_json, str)
        self.assertIsInstance(base_to_json, str)

        self.assertIsInstance(empty, list)
        self.assertIsInstance(rect_to_empty_json, str)
        self.assertIsInstance(base_to_empty_json, str)

        rect_from_json = Rectangle.from_json_string(rect_to_json)
        base_from_json = Base.from_json_string(rect_to_json)

        self.assertIsInstance(rect_from_json, list)
        self.assertIsInstance(base_from_json, list)

    def test_create(self):
        """instance create and attr """
        self.assertIsNotNone(self.sq2.__init__)
        self.assertIsNotNone(self.rt2.__dict__)

        attrs = ["width", "height", "x", "y", "id"]
        for attr in attrs:
            self.assertTrue(hasattr(self.rt2, attr))

        rt_dict = self.rt3.to_dictionary()
        rt_create = Rectangle.create(**rt_dict)
        self.assertEqual(self.rt3.__str__(), '[Rectangle] (100) 3/3 - 30/30')

    def test_load_file(self):
        """check method is loading file"""
        self.assertTrue(os.path.isfile('Rectangle.json'))
        with open('Rectangle.json') as file:
            for line in file:
                self.assertEqual(type(line), str)

        list_of_obj = [self.rt1, self.rt2, self.rt3]
        for obj in list_of_obj:
            self.assertIsInstance(obj, Rectangle)
            self.assertIsInstance(obj, Base)

        list_of_output = Rectangle.load_from_file()
        for rect in list_of_output:
            self.assertIsInstance(rect, Rectangle)

        Rectangle.save_to_file(list_of_obj)
        with open('Rectangle.json', mode='r') as file:
            count = 0
            for line in file:
                count += 1
            self.assertGreater(count, 0)

if __name__ == '__main__':
    unittest.main()
