def add_security(func):
   def wrapper():
       print("1. Before the function is called")
       print("2. Add helmet, gloves, knee support, license")
       func()
       print("3. After the function is called")
       print("4. Secure driving , leave all the items")

   wrapper()

@add_security
def driving_scooty():
    print("Normal function")
    print("I am driving the scooty")

@add_security
def driving_ola_scooty():
    print("ola")


