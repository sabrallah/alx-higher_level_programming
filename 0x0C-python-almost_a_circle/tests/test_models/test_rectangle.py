#!/usr/bin/python3
"""
mod contain test case for Rectangle class.
"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    test case for the rectangle class.
    """

    def test_init(self):
        """
        test initialization Rectangle class.
        """
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(3, 4, 5, 6, 7)
        self.assertEqual(r2.width, 3)
        self.assertEqual(r2.height, 4)
        self.assertEqual(r2.x, 5)
        self.assertEqual(r2.y, 6)
        self.assertEqual(r2.id, 7)

    def test_area(self):
        """
        test method of the Rectangle class.
        """
        r1 = Rectangle(2, 3)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(4, 5)
        self.assertEqual(r2.area(), 20)

    def test_display(self):
        """
        display method Rectangle class tested.
        """
        r1 = Rectangle(2, 3, 1, 1)
        expected = "\n" \
                   " #\n" \
                   "###\n"
        self.assertEqual(r1.display(), expected)

        r2 = Rectangle(4, 5, 2, 2)
        expected = "\n" \
                   "    ####\n" \
                   "    ####\n" \
                   "    ####\n" \
                   "    ####\n" \
                   "    ####\n"
        self.assertEqual(r2.display(), expected)


if __name__ == '__main__':
    unittest.main()
