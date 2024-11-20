# Write a program for sum of three numbers from user input
#if user doesn't enter any number, use default 100,200,300


num1 = int(input("Enter the first number\n"))
num2 = int(input("Enter the Second number\n"))
num3 = int(input("Enter the third number\n"))

def sum_of_three_num(num1=100, num2=200, num3=300):
    return num1+num2+num3
result= sum_of_three_num(num1,num2,num3)
print(result)

result2= sum_of_three_num()
result2= sum_of_three_num(2)
result2= sum_of_three_num(3,4)
result2= sum_of_three_num(4,6,7)
print(result2)

