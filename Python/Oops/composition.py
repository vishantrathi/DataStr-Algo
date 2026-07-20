#Composition--> in composition we build obj out of other objs

# |----------------|         |---------------|
# |     BOOK       |         |    AUTHOR     |
# |     TITLE      |         |FIRST NAME     |
# |     PRICE      |         |SECOND NAME    |
# |     AUTHOR-----|-------->|               |
# |----------------|         |---------------|

class Book:
    def __init__(self,title,price,authorfName,authorlName):
        self.title=title
        self.price=price
        self.authotfName=authorfName
        self.authorlName=authorlName
        self.chapter=[]

    def addchapter(self,chapter):
        self.chapter.append(chapter)

    def getbookcount(self):
        result=0
        for ch in self.chapter:
            result+=ch.pagecount
        return result

class Author:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

    def __str__(self):
        return f"{self.fname}{self.lname}"
    
class Chapter:
    def __init__(self,name,pagecount):
        self.name=name
        self.pagecount=pagecount


auth=Author("leo","tolstiry")
b1=Book("war and peace",39.0,"leo","tolstoy")

b1.addchapter(Chapter("chapter1",1))
b1.addchapter(Chapter("chapter2",2))
b1.addchapter(Chapter("chapter3",3))

print(b1.title)
