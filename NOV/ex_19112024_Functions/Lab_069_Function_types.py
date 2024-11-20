# 1 User defined

#1. They can't return -> not return
#2. They can return something
#3. They have parameters
#4. They don't have parameters



#1. They can't return -> not return
# No arguments and not return

def greet():
    print("Hello")
greet()
print("-----------------------------------")
#2. They have parameters but not return

def greet(name):
    print("Hello" , name)
greet("Shubham")


#3. Not return but default arguments

def say_hello_default_argument(name="Shubham"):
    print("Hello", name.upper())
say_hello_default_argument("Goel")
say_hello_default_argument()

def multiple_Argument(name1="A", name2="B"):  #default argument or positional argumet
    print("Hello ->", name1,name2)
multiple_Argument()
multiple_Argument("Shubham","Goel")
multiple_Argument("Shubham", "Amit")


#4. Arguments + return type

def sum_of_two(a,b):
    return a+b
result=sum_of_two(4,5)

print(result)


def sum_of_two(a=55,b=90):
    return a+b
result=sum_of_two()

print(result)





