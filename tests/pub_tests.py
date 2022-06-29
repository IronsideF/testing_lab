import unittest
from src.pub import Pub

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub("The Queen's Arm", 100.00, self.drinks_list)

    def test_pub_has_name(self):
        self.assertEqual("The Queen's Arm", self.pub.name)