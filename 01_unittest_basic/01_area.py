import unittest


def area(width, height):
    try:

            return width * height

    except TypeError:
        print("Value must be int > 0")


class TestArea(unittest.TestCase):

    def test_normal_area(self):
        self.assertEqual(area(4, 5), 20)

    def test_area_string_parametr(self):
        self.assertRaises(TypeError, area('4', 5))

    def test_area_negative_value(self):
        self.assertRaises(ValueError, area, -1, 2)


if __name__ == '__main__':
    unittest.main(verbosity=2)

