class Customer:
    def __init__(self, _name, _wallet):
        self.name = _name
        self.wallet = _wallet

    def remove_money(self, amount_change):
        self.wallet -= amount_change
