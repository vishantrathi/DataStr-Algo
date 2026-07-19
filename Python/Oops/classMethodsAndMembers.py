#using class level and ststic method
class Book:
    #properties define at class level shared by all instances
    Book_Type=("HardCover","Paperback","EBook")

    #double underscore properties are hodden from other classes
    __booklist=None

    # create a class method
    @classmethod
    def get_book_type(cls):
        return cls.Book_Type
    
    #create a ststic method
    def get_bookList():
        if Book.__booklist==None:
            Book.__booklist=[]
        return Book.__booklist

    def set_title(self,newtitle):
        self.title=newtitle
    
    def __init__(self,title):
        self.title=title
        if(not self.Book_Type in Book.Book_Type):
            raise ValueError(f'{self.Book_Type} is not valid!')
        else:
            self.Book_Type=self.Book_Type
        
#access the attribute

print("Book types:",Book.get_book_type())
#book instance

b1=Book("Title1","HardCover")