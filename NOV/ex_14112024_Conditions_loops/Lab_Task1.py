# Write a program for Checking for a Leap Year

year = int(input("Enter the year\n"))

# if year % 4==0 and year % 100!=0:
#     print("it is a leap year",year)
# elif year % 400 ==0 and year % 100 ==0:
#     print("it is a leap year", year)
# else:
#     print("it is not leap year")

if (year % 4==0 and year % 100!=0) or(year % 400 == 0):
    print("it is a leap year",year)
else:
    print("it is not leap year")


