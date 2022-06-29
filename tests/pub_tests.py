import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer
from src.food import Food

class TestPub(unittest.TestCase):
    def setUp(self):
        self.drink1 = Drink("beer", 5, 1)
        self.drink2 = Drink("vodka", 6, 3)
        self.drink3 = Drink("tequila", 8, 5)
        drinks = {
            'beer': self.drink1,
            'vodka': self.drink2,
            'tequila': self.drink3
        }
        self.food1 = Food("crisps", 2, 1)
        self.food2 = Food("peanuts", 3, 2)
        food_list = [self.food1, self.food2]
        stock = {
            'beer': 25,
            'vodka': 15,
            'tequila': 12
        }
        self.pub = Pub("The Queen's Arm", 100.00, drinks, food_list, stock)

    def test_pub_has_name(self):
        self.assertEqual("The Queen's Arm", self.pub.name)
    
    def test_pub_has_till(self):
        self.assertEqual(100.00, self.pub.till)

    def test_pub_has_drinks(self):
        self.assertEqual(3, len(self.pub.drinks))

    def test_pub_can_add_money(self):
        self.pub.add_money(5.00)
        self.assertEqual(105.00, self.pub.till)

    def test_pub_can_find_drink(self):
        self.assertEqual(self.drink1, self.pub.find_drink_by_name('beer'))

    def test_pub_can_find_drink_not_found(self):
        self.assertEqual(None, self.pub.find_drink_by_name('wkd'))

    def test_pub_can_sell_drink(self):
        customer = Customer("Jon", 35, 100.00)
        self.pub.sell_drink(customer, "beer")
        self.assertEqual(self.pub.till, 105.00)
        self.assertEqual(customer.wallet, 95.00)
        self.assertEqual(1, customer.drunkeness)
        self.assertEqual(24, self.pub.stock['beer'])
        
    def test_pub_check_age(self):
        customer = Customer('Jon', 30, 100.00)
        self.assertEqual(True, self.pub.find_customer_age(customer))

    def test_pub_check_age_false(self):
        customer = Customer('Timmy', 13, 100.00)
        self.assertEqual(False, self.pub.find_customer_age(customer))

    def test_pub_can_sell_drink_underage(self):
        customer = Customer('Timmy', 13, 100.00)
        self.pub.sell_drink(customer, "tequila")
        self.assertEqual(self.pub.till, 100.00)
        self.assertEqual(customer.wallet, 100.00)

    def test_pub_can_sell_drink_too_drunk(self):
        customer = Customer("Keith", 48, 100.00)
        customer.drunkeness = 12
        self.pub.sell_drink(customer, "tequila")
        self.assertEqual(self.pub.till, 100.00)
        self.assertEqual(customer.wallet, 100.00)

    def test_pub_has_food(self):
        self.assertEqual(2, len(self.pub.food_list))
    
    def test_pub_can_sell_drink_not_found(self):
        customer = Customer("Keith", 48, 100.00)
        self.pub.sell_drink(customer, "jack and coke")
        self.assertEqual(self.pub.till, 100.00)
        self.assertEqual(customer.wallet, 100.00)
    
    def test_pub_find_food(self):
        self.assertEqual(self.food1, self.pub.find_food_by_name('crisps'))

    def test_pub_food_not_found(self):
        self.assertEqual(None, self.pub.find_food_by_name('hot dog'))

    def test_pub_can_sell_food(self):
        customer = Customer('Jon', 30, 100.00)
        customer.drunkeness = 10
        self.pub.sell_food(customer, 'peanuts')
        self.assertEqual(self.pub.till, 103.00)
        self.assertEqual(customer.wallet, 97.00)
        self.assertEqual(8, customer.drunkeness)

    def test_pub_can_sell_drink_no_money(self):
        customer = Customer("keith", 48, 3.00)
        self.pub.sell_drink(customer, 'tequila')
        self.assertEqual(self.pub.till, 100.00)
        self.assertEqual(customer.wallet, 3.00)
        self.assertEqual(0, customer.drunkeness)

    def test_pub_has_stock(self):
        self.assertEqual(25, self.pub.stock['beer'])
    
    def test_pub_gets_stock_value(self):
        self.assertEqual(311, self.pub.stock_value())



