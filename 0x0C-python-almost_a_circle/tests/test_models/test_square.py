#!/usr/bin/python3
"""
containhe test case for Square classes.
"""

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    for the Square class test case.
    """

    def test_init(self):
        """
        test initialization Square class.
        """
        s1 = Square(1)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, 1)

        s2 = Square(2, 3, 4, 5)
        self.assertEqual(s2.size, 2)
        self.assertEqual(s2.x, 3)
        self.assertEqual(s2.y, 4)
        self.assertEqual(s2.id, 5)

    def test_str(self):
        """
        the __str__ method Square class.
        """
        s1 = Square(1, 2, 3, 4)
        expected = "[Square] (4) 2/3 - 1"
        self.assertEqual(str(s1), expected)

        s2 = Square(2)
        expected = "[Square] (2) 0/0 - 2"
        self.assertEqual(str(s2), expected)

    def test_update(self):
        """
        the update method Square class.
        """
        s1 = Square(1)
        s1.update(2, 3, 4, 5)
        self.assertEqual(s1.size, 3)
        self.assertEqual(s1.x, 4)
        self.assertEqual(s1.y, 5)
        self.assertEqual(s1.id, 2)

        s2 = Square(2)
        s2.update(x=3, y=4, id=5)
        self.assertEqual(s2.size, 2)
        self.assertEqual(s2.x, 3)
        self.assertEqual(s2.y, 4)
        self.assertEqual(s2.id, 5)

    def test_to_dictionary(self):
        """
        the to_dictionary method Square class.
        """
        s1 = Square(1, 2, 3, 4)
        expected = {
            'id': 4,
            'size': 1,
            'x': 2,
            'y': 3
        }
        self.assertEqual(s1.to_dictionary(), expected)

        s2 = Square(2)
        expected = {
            'id': s2.id,
            'size': 2,
            'x': 0,
            'y': 0
        }
        self.assertEqual(s2.to_dictionary(), expected)


if __name__ == '__main__':
    unittest.main()
