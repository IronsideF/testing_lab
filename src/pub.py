class Pub:
    def __init__(self, _name, _till, _drinks):
        self.name = _name
        self.till = _till
        self.drinks = _drinks

    def add_money(self, amount_change):
        self.till += amount_change

    def find_drink_by_name(self, drink_name):
        for drink in self.drinks:
            if drink.name == drink_name:
                return drink

    def sell_drink(self, customer, drink_name):
        drink = self.find_drink_by_name(drink_name)
        customer.remove_money(drink.price)
        self.add_money(drink.price)
