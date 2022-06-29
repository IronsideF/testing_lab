import unittest
from src.drink import Drink
drinks_list =[]
class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink_1("Beer", 5)
        self.drink_2("Vodka", 6)
        self.drink_3("Tequila", 8)
        self.drinks_list = [self.drink_1, self.drink_2, self.drink_3]