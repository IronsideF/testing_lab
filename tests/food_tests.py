import unittest
from src.food import Food

class TestFood(unittest.TestCase):
    def setUp(self):
        self.food1 = Food("crisps", 2, 1)
    
    def test_food_has_name(self):
        self.assertEqual("crisps", self.food1.name)
    def test_food_has_price(self):
        self.assertEqual(2, self.food1.price)
    def test_food_has_rejuv(self):
        self.assertEqual(1, self.food1.rejuvenation_level)

