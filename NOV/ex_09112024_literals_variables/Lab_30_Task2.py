# Task 1 for the Today
# Take a 2 input from the user
# Print the Quotient and Remainder
# 15 ->  num1
# 2 -> num2
# Q -> 7
# R -> 1

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the Second number:"))

Q = num1//num2
R = num1%num2

print("Quotient of numbers is",Q)
print("Reminder of numbers is",R)