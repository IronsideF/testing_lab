class Customer:
    def __init__(self, _name,_age, _wallet):
        self.name = _name
        self.age = _age
        self.wallet = _wallet
        self.drunkeness = 0

    def remove_money(self, amount_change):
        self.wallet -= amount_change
    def add_drunkeness(self, drink):
        self.drunkeness += drink.alcohol_level
    def reduce_drunkeness(self, food):
        self.drunkeness -= food.rejuvenation_level