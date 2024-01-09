import unittest
from fizzbuzz import fizzbuzz

class FizzBuzzTestCase(unittest.TestCase):

    def test_2(self):
        result = fizzbuzz(2)
        self.assertEqual(result, 2)

    def test_3(self):
        result = fizzbuzz(3)
        self.assertEqual(result, "Fizz")
    
    def test_4(self):
        result = fizzbuzz(4)
        self.assertEqual(result, 4)

    def test_5(self):
        value = 5 # ARRANGE
        result = fizzbuzz(value) # ACT
        self.assertEqual(result, "Buzz") # Assert

unittest.main()