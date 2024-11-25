# Write a program to find even or odd number

# def Even_odd_number(num):
#     if num % 2 == 0:
#         print("even")
#     else:
#         print("Odd")
#
# Even_odd_number(3)

#using lambda function

n= int(input("Enter the number\n"))
Even_odd_number = lambda num : "Even "if n % 2==0 else "odd"
print(Even_odd_number(n))

