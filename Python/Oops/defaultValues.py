from dataclasses import dataclass, field
import random

def price_func():
    return float(random.randrange(0,10))

@dataclass
class Book:
    title:str="No Title"
    author:str="No Author"
    pages:int=0
    price:float=field(default_factory=price_func)

b2=Book("War and Love","Leo",1252)
b3=Book("the new ages of tech","me&youorUS",1)


print(b2)
print(b3)