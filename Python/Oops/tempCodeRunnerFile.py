def __eq__(self,value): #checks for eq betn two objects
        if not isinstance(value,Book):
            raise ValueError("can't compair book to a non-book")
        return(self.title==value.title and
               self.author==value.author and
               self.price==value.price)