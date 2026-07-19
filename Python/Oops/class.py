class book:
    def __init__(self,title) :
        self.title=title
#creating instance of the classes
book1=book("Brave New World")
book2=book("War and Peace")

print(book1.title)
print(book2.title)