import unittest
from converter import celsius_to_fahrenheit, fahrenheit_to_celsius, parse_temperature

class TestConverter(unittest.TestCase):
    def test_celsius_to_fahrenheit(self):
        self.assertEqual(celsius_to_fahrenheit(0), 32.0)
        self.assertEqual(celsius_to_fahrenheit(100), 212.0)
        self.assertEqual(celsius_to_fahrenheit(-40), -40.0)
        self.assertEqual(celsius_to_fahrenheit(37), 98.6)
        self.assertEqual(celsius_to_fahrenheit(36.6), 97.88)
        self.assertEqual(celsius_to_fahrenheit(-273.15), -459.67)
        self.assertEqual(celsius_to_fahrenheit(" +37 "), 98.6)
        
    def test_fahrenheit_to_celsius(self):
        self.assertEqual(fahrenheit_to_celsius(32), 0.0)
        self.assertEqual(fahrenheit_to_celsius(212), 100.0)
        self.assertEqual(fahrenheit_to_celsius(-40), -40.0)
        self.assertEqual(fahrenheit_to_celsius(98.6), 37.0)
        self.assertEqual(fahrenheit_to_celsius(-459.67), -273.15)
        self.assertEqual(fahrenheit_to_celsius(" +32 "), 0.0)

    def test_absolute_zero_rejection(self):
        with self.assertRaises(ValueError):
            celsius_to_fahrenheit(-274)
        with self.assertRaises(ValueError):
            fahrenheit_to_celsius(-460)

    def test_invalid_input(self):
        invalid_inputs = ["abc", "", None, float('inf'), float('nan')]
        for val in invalid_inputs:
            with self.assertRaises(ValueError):
                celsius_to_fahrenheit(val)
            with self.assertRaises(ValueError):
                fahrenheit_to_celsius(val)

    def test_round_trip(self):
        c_initial = 25.5
        f = celsius_to_fahrenheit(c_initial)
        c_final = fahrenheit_to_celsius(f)
        self.assertAlmostEqual(c_initial, c_final, places=2)

if __name__ == '__main__':
    unittest.main()
