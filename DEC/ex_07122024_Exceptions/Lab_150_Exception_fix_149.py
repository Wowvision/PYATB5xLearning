print("----Start of the program")
try:
     a= int(input("Enter the num1"))   #ValueError: invalid literal for int() with base 10: 'shubham'
     b= int(input("Enter the num2"))

     c= a /b          #ZeroDivisionError: division by zero
     print("The division of",c)
except Exception as e:
     print(e)
print("------End of the program")