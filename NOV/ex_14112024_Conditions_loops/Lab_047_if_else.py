# Program to find maximum between 3 numbers

num1 = int(input("Enter the first number\n"))
num2 = int(input("Enter the Second number\n"))
num3 = int(input("Enter the third number\n"))

if num1 > num2 and num1 > num3:
    print("num1 is max", num1)
elif num2 > num3 and num2 > num3:
    print("num2 is max", num2)
else:
    print("num3 is max", num3)
