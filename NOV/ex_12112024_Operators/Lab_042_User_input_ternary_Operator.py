# Program if age >18 allowed to vote
# else not allowed to vote

User_age = int(input("Enter user age\n"))

if User_age > 18:
    print("Yes can go to GOA and vote")

else:
    print("Not You can't go GOA and vote")
#
#using above thing in ternary
#print("Yes can go to GOA and vote" if User_age > 18 else "Not You can't goa and vote")
#print("Yes can go to GOA and vote" if int(input("Enter user age\n")) > 18 else "Not You can't goa and vote")