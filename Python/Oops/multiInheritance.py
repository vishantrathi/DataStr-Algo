class A:
    def __init__(self):
        super().__init__()
        self.propl="propl"
        self.name="ClassA"

class B:
    def __init__(self):
        super().__init__()
        self.prop2="prop2"
        self.name="ClassB"

class C(A, B): #the control goes from left to right
    def __init__(self):
        super().__init__()  # super init parent class k constructor ko call karta hai

    def showprops(self):
        print(self.propl)
        print(self.propl)
        print(self.name) #print class A for this it usues method resolution 

c=C()
c.showprops()