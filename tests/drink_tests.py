import unittest
from src.drink import Drink
class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink_1 = Drink("Beer", 5)
    
    def test_drink_has_name(self):
        self.assertEqual("Beer", self.drink_1.name)
    
    def test_drink_has_price(self):
        self.assertEqual(5, self.drink_1.price)