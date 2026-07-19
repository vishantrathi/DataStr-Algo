class stock():
    def __init__(self,Ticker,Price,Company):
        self.Ticker=Ticker
        self.Price=Price
        self.Company=Company

    def get_description(self):
        return (f'Stock{self.Ticker},{self.Price},{self.Company}')
    
symbol = stock("GOOG", 183.45, "Google LLC")
print(symbol.get_description())