class book:
    def __init__(self,title,author,pages,price,discount) :
        self.title=title
        self.author=author
        self.pages=pages
        self.price=price
        self._discount=discount
        
    
    def getprice(self):
        if hasattr(self,"_discount"):  #self is a reference to the current object (instance) of the class. It allows an object to access its own variables and methods.
            return self.price-(self.price*self._discount)
        else:
            return self.price
    
    def setDiscount(self,amount):
        self._discount= amount

    
#creating instance of the classes

book1=book("Brave New World",122,39,100,0.25)
book2=book("War and Peace",234,29,100,0.25)


book2.setDiscount(0.25)
print(book1.title,book1.getprice())
print(book2.title,book2.getprice())