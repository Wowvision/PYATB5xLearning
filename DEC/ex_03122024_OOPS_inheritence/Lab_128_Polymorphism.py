#Method Overloading

class Dog:

    def bark(self):
        print("Dog is barking")

    def bark(self, breed):
        self.breed = breed
        print("dog with breed is barking", breed)

d_ref = Dog()
d_ref.bark("Chow")