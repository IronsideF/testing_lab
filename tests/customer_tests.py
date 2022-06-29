from __future__ import unicode_literals
import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer1 = Customer("Keith", 30, 100.00)

    def test_customer_has_name(self):
        self.assertEqual("Keith", self.customer1.name)

    def test_customer_has_wallet(self):
        self.assertEqual(100.00, self.customer1.wallet)

    def test_customer_can_remove_money(self):
        self.customer1.remove_money(5.00)
        self.assertEqual(95.00, self.customer1.wallet)

    def test_has_age(self):
        self.assertEqual(30, self.customer1.age)

    def test_customer_has_drunkeness(self):
        self.assertEqual(0, self.customer1.drunkeness)
    