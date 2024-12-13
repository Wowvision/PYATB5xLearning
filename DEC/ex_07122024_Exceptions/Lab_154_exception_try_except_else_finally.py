try:

    a = int(input("Enter the num1"))
    b = int(input("Enter the num2"))
    c = a /b
except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
else:
 print("the result is : ",c)

finally:
    print("This code will always executed")