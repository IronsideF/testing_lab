import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    def setUp(self):
        self.drink1 = Drink("beer", 5)
        self.drink2 = Drink("vodka", 6)
        self.drink3 = Drink("tequila", 8)
        drinks_list = [self.drink1, self.drink2, self.drink3]
        self.pub = Pub("The Queen's Arm", 100.00, drinks_list)

    def test_pub_has_name(self):
        self.assertEqual("The Queen's Arm", self.pub.name)
    
    def test_pub_has_till(self):
        self.assertEqual(100.00, self.pub.till)

    def test_pub_has_drinks(self):
        self.assertEqual(3, len(self.pub.drinks))

    def test_pub_can_add_money(self):
        self.pub.add_money(5.00)
        self.assertEqual(105.00, self.pub.till)

    def test_pub_can_sell_drink(self):
        customer = Customer("Jon", 100.00)
        self.pub.sell_drink(customer, "beer")
        self.assertEqual(self.pub.till, 105.00)
        self.assertEqual(customer.wallet, 95.00)
