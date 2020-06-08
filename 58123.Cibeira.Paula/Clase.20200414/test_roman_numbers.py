import unittest
from roman_numbers import roman_to_decimal


class TestRomanNumbers(unittest.TestCase):
<<<<<<< HEAD

    def test_roman_I_to_decimal(self):
        decimal_number = roman_to_decimal('I')
        self.assertEqual(decimal_number, 1)

    def test_roman_II_to_decimal(self):
        decimal_number = roman_to_decimal('II')
        self.assertEqual(decimal_number, 2)

=======
    def test_roman_I_to_decimal(self):
        decimal_number = roman_to_decimal('I')
        self.assertEqual(decimal_number, 1)
    def test_roman_I_to_decimal(self):
        decimal_number=roman_to_decimal("II")    
        self.assertEqual(decimal_number, 2)
    
>>>>>>> 908be912e2f06a2db1dbef498019d1ccf5675100

if __name__ == '__main__':
    unittest.main()
