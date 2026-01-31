class Security:
    def __init__(self, name:str, symbol:str, price:float):
        self.name = name          
        self.symbol = symbol      
        self.price = price 

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    def calculate_value(self, quantity: int):
        return self.price * quantity

    def __str__(self):
        return f"Name:{self.name}, {self.symbol}, Price: {self.price}$"
    