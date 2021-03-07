import unittest


class TestClass(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual("Adam Kawior".split(), ["Adam", "Kawior"])

    def test_case_2(self):
        self.assertEqual("%".join(["Adam", "Kawior"]), "Adam%Kawior")