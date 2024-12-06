# Take a input and create the clas

class Person:

    def __init__(self):
        print("I will be called")
        self.name = input("Enter the name\n")
        self.age = input("Enter the age\n")
        self.phone = input("Enter the phone\n")
        self.occupation = input("Enter the Occupation\n")

    def name_of_the_function_to_display(self):
        print("Name is",self.name,"Age is", self.age,"phone number is", self.phone,
              "Occupation is",self.occupation)

person1 = Person()
person1.name_of_the_function_to_display()