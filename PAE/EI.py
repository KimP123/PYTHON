class Computer:
    def __init__ (self, max_price):
        self.__max_price = max_price
    
    def sell(self):
        print(f'Selling Price: ${self.__max_price}')

    def set_max_price(self,price):
        self.__max_price = price

comp1 = Computer(1000)
comp1.sell()

comp1.__max_price = 1200
comp1.sell()

comp1.set_max_price(1200)
comp1.sell()