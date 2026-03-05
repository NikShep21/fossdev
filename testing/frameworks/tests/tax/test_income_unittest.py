import unittest
from tax.income import calculate_tax

class TestCalculateTax(unittest.TestCase):
    def test_income(self):
        self.assertEqual(calculate_tax(1000), 130.00)
        
    def test_integers_cents(self):
        self.assertEqual(calculate_tax(1234.56), 160.49)

if __name__ == '__main__':
    unittest.main()