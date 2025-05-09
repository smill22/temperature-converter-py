# test_temperature_converter.py

import unittest
from temperature_converter import TemperatureConverter

class TestTemperatureConverter(unittest.TestCase):

    def setUp(self):
        self.converter = TemperatureConverter()

    def test_celsius_to_fahrenheit(self):
        result = self.converter.celsius_to_fahrenheit(0)
        self.assertEqual(result, 32)

        result = self.converter.celsius_to_fahrenheit(100)
        self.assertEqual(result, 212)

    def test_fahrenheit_to_celsius(self):
        result = self.converter.fahrenheit_to_celsius(32)
        self.assertAlmostEqual(result, 0)

        result = self.converter.fahrenheit_to_celsius(212)
        self.assertAlmostEqual(result, 100)

if __name__ == '__main__':
    unittest.main()
