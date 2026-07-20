class Book:
    def __init__(self,title,author,price):
        super().__init__()
        self.title=title
        self.author=author
        self.price=price
        pass

    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"
    
    def __repr__(self):
        return f"{self.title},author={self.author}, price={self.price}"
    
    def __eq__(self,value): #checks for eq betn two objects
        if not isinstance(value,Book):
            raise ValueError("can't compair book to a non-book")
        return(self.title==value.title and
               self.author==value.author and
               self.price==value.price)
    
    def __ge__(self,value): # establish relationship >= betn two objs
        if not isinstance(value,Book):
            raise ValueError("can't compair book to a non-book")
        return self.price >=value.price
    
    def __lt__(self, value): #used to sort(less than)
        if not isinstance(value, Book):
            raise ValueError("can't compare book to a non-book")
        return self.price < value.price

    
b1=Book("War and Peace", "leo Tol",36.25)
b2=Book("The vatcxher", "noud sgv",322.5)
b3=Book("mood love", "nsj sg",32.55)
b4=Book("mood love", "nsj sg",32.55)

# print(b1)
# print(b2)
# print(b1==b2)
# print(b1==b3)
# print(b3==b4)
# # print(b3==89) # raise value
# print(b1>=b2)
# print(b1<=b2)
# print(str(b1))  # return human readable string
# print(repr(b2)) #return developer friendly representation

Books=[b1,b2,b3,b4]
Books.sort()
print([book.title for book in Books])
