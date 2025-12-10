import unittest

from day3 import get_joltage


class TestDay3(unittest.TestCase):

    def test_short(self):
        self.assertEqual(23, get_joltage("123", 2))

    def test_mid(self):
        self.assertEqual(54, get_joltage("225341", 2))

    def test_long(self):
        self.assertEqual(87, get_joltage("65422318111112224766666644555", 2))

    def test_three_flips(self):
        self.assertEqual(887, get_joltage("8855555557", 3))


    def test_twelve_flips(self):
        self.assertEqual(987654321111, get_joltage("987654321111111", 12))