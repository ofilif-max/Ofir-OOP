from security import *

class Stock(Security):
    def __init__(self, name: str, symbol: str, price: float, dividend: float):
        super().__init__(name, symbol, price)
        self.dividend = dividend 
    
    def dividend_yield(self): 
        if self.price == 0:
            return 0
        return (self.dividend / self.price) * 100
    
    def __str__(self):
        return f"{super().__str__()}, Dividend: {self.dividend}$"



class Bond(Security):
    def __init__(self, name: str, symbol: str, price: float, interest_rate: float):
        super().__init__(name, symbol, price)
        self.interest_rate = interest_rate

    def annual_interest_gain(self):
        return self.price * (self.interest_rate / 100)

    def __str__(self):
        return f"{super().__str__()}, Interest Rate: {self.interest_rate}%"



class Option(Security):
    def __init__(self, name, symbol, price, strike_price):
        super().__init__(name, symbol, price)
        self.strike_price = strike_price 
    
    def is_profitable(self):
        return self.price > self.strike_price

    def __str__(self):
        return f"{super().__str__()}, Strike Price: {self.strike_price}$"