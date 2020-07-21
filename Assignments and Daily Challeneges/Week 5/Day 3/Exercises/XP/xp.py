class Currency():
    def __init__(self, value, currency):
        self.value = float(value)
        self.currency = currency

#   * currency + 5
#     * currency  +  another_currency  (if they have the same label, otherwise raise an error)
    def __repr__(self):
        return f"The value of your {self.currency} is {self.value}."
    
    def __add__(self, other_currency):
        if self.currency == other_currency.currency:
            print(self.value + other_currency.value)
        else:
            raise "Not the same currency."


dollar = Currency(10, "Dollars")
dollar2 = Currency(15, "Dollars")
dollar3 = Currency(20, "Shekels")

print(dollar.__add__(dollar2))