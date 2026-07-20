class Book:
    def __init__(self,title,author,price):
        super().__init__()
        self.title=title
        self.author=author
        self.price=price
        self.discount=0.1
        pass

    def __str__(self):  # used to get the user friendly string
        return f"{self.title} by {self.author}, costs {self.price}"
    
    def __getattribute__(self, name):  #Called for every attribute access
        if name=="price":
            p=super().__getattribute__("price")
            d=super().__getattribute__("discount")
            return p - (p*d)
        return super().__getattribute__(name)
    
    def __setattr__(self, name, value): #every time you assign a value to an attribute.
        if name == "price":
            if not isinstance(value, float):
                raise ValueError(" the price is not in float")
        return super().__setattr__(name,value)
    
    def __getattr__(self, name): #Called only if the attribute doesn't exist
        return name + "is not here"
    
    def __call__(self,title,author,price):  #used to call object like a function
        self.title=title
        self.author=author
        self.price=price
    

b1=Book("War and Peace", "leo Tol",36.25)
b2=Book("The vatcxher", "noud sgv",322.5)
b3=Book("mood love", "nsj sg",32.55)
b4=Book("mood love", "nsj sg",32.55)

b1.price=float(40)
b1(" annna karima","leo",78.32)
print(b1)
    