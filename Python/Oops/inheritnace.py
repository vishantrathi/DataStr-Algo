class publications:
    def __init__(self,title,price):
        self.title=title
        self.price=price

class book(publications):# inherited the publication by  book
    def __init__(self,title,author,pages,price):
        super(). __init__(title,price) # iss line ka matlb hai ki parants publication ka constuctor call karo
        self.title=title
        self.price=price
        self.author=author
        self.pages=pages

class Periodical(publications):
    def __init__(self, title, price,period,publisher):
        super().__init__(title, price)
        self.period=period
        self.publisher=publisher

class Magazine(Periodical):
    def __init__(self,title,publisher,price,period):
        super().__init__(title,price,period,publisher)
        

class Newspaper():
    def __init__(self,title,publisher,price,period):
        super().__init__(title,price,period,publisher)

b1=book('New Ways Of Life','Evergreen',499,2011)
n1=Magazine("NY Times","NY Times Company",6.0,1985)


print(b1.author)
print(n1.publisher)