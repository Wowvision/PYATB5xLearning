


class Person:

    def __init__(self,name):
        self.name = name

    def walk(self):
        return self.name

Amit = Person("amit")
Shubham = Person("Shubham")

print("Who is walking",Amit.walk())
print("Who is walking", Shubham.walk())

print(Amit.name)
print(Shubham.name)