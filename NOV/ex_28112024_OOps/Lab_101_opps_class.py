class Persion:
# Attributes  ->What you have?
    id : None
    Name : None
    age : None
    email : None
    height : None
    gender : None
    Phone_num : None
    Address : None

# Behaviour -> What you can do?
    def talk(self):    #NRNG  this, self will first argument in every
        print("I can talk")

    def sleep(self, name):   #arguement with no return
        print("I am a method")
        print("Sleep" , name)

    def sleep2(self, name):   #arguement with return
        print("I am a method")
        return None

    def walk(self):
        print("I am walking")

    def walk_return(self):    #NO argument with return
        return "I am walking"


# Create the object of the class
# ObjectRef =  ClassName() -> Object

geeta = Persion()
geeta.name = "Geeta Sharma"
geeta.gender = "Female"


