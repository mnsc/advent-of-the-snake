import unittest

from day3 import get_joltage


class TestDay3(unittest.TestCase):

    def test_short(self):
        self.assertEqual(23, get_joltage("123"))

    def test_mid(self):
        self.assertEqual(54, get_joltage("225341"))

    def test_long(self):
        self.assertEqual(87, get_joltage("65422318111112224766666644555"))