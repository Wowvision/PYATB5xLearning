class Dog:
    #Attribute
    name= None
    breed = None
    height = None
    weight = None


    def __init__(self):
        print("I will be called")

    def Bark(self):
        print("Barking")

    def Sleep(self):
        print("Sleeping")

    def talk(self):
        pass

chow_ref = Dog()
mow_ref = Dog()

print(chow_ref.name)
print(mow_ref.name)

