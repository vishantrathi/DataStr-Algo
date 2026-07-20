from dataclasses import dataclass

@dataclass
class Book:
    title: str
    authorfName: str
    authorlName: str
    price: float

    def bookinfo(self):
        return f"{self.title}, by {self.authorfName} {self.authorlName}"

    def __post_init__(self):
        self.description = f"{self.title} by {self.authorfName} {self.authorlName}"


b1 = Book("war and peace", "leo", "tolstoy", 39.0)
b2 = Book("new way of world", "ss", "tww", 39.0)

print(b1.title)
print(b1 == b2)

b1.title = "new ways 2"
print(b1)
print(b1.description)