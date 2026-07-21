from dataclasses import dataclass, field
import random

def price_func():
    return float(random.randrange(0,10))

@dataclass(frozen=True)  # it is used to declare to use for the value , which are not going to change in future
class ImmutableClass:
    value1:str="Value1"
    value2:int=0

    def some_func(self,newval):
        self.value2=newval

obj=ImmutableClass("Another String",10)
print(obj.value1,obj.value2)

# obj.value1="Aother string"
# print(obj.value1)  # frzen instace error

obj.some_func(20) # frzen instace error