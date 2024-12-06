class Dog:
    #Attribute
    name= None
    breed = None
    height = None
    weight = None


    def __init__(self, name, breed):   #parameterized constructor
        print("I will be called")
        self.name = name
        self.breed = breed

    def Bark(self):
        print("Barking")

    def Sleep(self):
        print("Who is sleep",self.name)

    def talk(self):
        pass

chow_ref = Dog("chow",  "BB")
print(id(chow_ref.name))
chow_ref.Sleep()

mow_ref = Dog("mow", "huski")
print(id(mow_ref.name))
mow_ref.Sleep()

#Dog()  #object without reference