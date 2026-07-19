#An abstract class is a class that cannot be used to create objects directly.
#It acts as a blueprint for other classes and forces child classes to implement certain methods.
from abc import ABC, abstractmethod

class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    #Jo bhi class GraphicShape ko inherit karegi, usse calArea() implement karna hi hoga.
    @abstractmethod
    def calArea(self):
        pass

#circle ne calArea() implement kiya.
#haa
#Isliye circle ka object ban sakta hai.
class circle(GraphicShape):
    def __init__(self,radius):
        self.radius=radius
    def calArea(self):
        return 3.14*(self.radius**2)

class square(GraphicShape):
    def __init__(self,side):
        self.side=side
    def calArea(self):
        return self.side*self.side

# g=GraphicShape()


c=circle(10)
s=square(12)
print(s.calArea())