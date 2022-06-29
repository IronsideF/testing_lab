class Pub:
    def __init__(self, _name, _till, _drinks, _food, _stock):
        self.name = _name
        self.till = _till
        self.drinks = _drinks
        self.limit = 10
        self.food_list = _food
        self.stock = _stock

    def add_money(self, amount_change):
        self.till += amount_change

    def find_drink_by_name(self, drink_name):
        for drink in self.drinks:
            if drink.name == drink_name:
                return drink

    def find_customer_age(self, customer):
        return customer.age >= 18

    def sell_drink(self, customer, drink_name):
        if self.find_customer_age(customer) and customer.drunkeness < self.limit:
            drink = self.find_drink_by_name(drink_name)
            if drink != None and customer.wallet >= drink.price:
                customer.remove_money(drink.price)
                self.add_money(drink.price)
                customer.add_drunkeness(drink)

    def find_food_by_name(self, food_name):
        for dish in self.food_list:
            if dish.name == food_name:
                return dish
    
    def sell_food(self, customer, food_name):
        dish = self.find_food_by_name(food_name)
        if dish != None and customer.wallet >= dish.price:
            customer.remove_money(dish.price)
            self.add_money(dish.price)
            customer.reduce_drunkeness(dish)

