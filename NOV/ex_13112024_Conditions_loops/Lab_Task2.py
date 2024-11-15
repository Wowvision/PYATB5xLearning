#Write a program that classifies a triangle based on its side lengths.
# Given three input values representing the lengths of the sides,
# determine if the triangle is equilateral (all sides are equal),
# isosceles (exactly two sides are equal), or scalene (no sides are equal).
# Use an if-else statement to classify the triangle.

#s1, s2, s3 ->int

s1 = int(input("Enter the first side value of triangle\n"))
s2 = int(input("Enter the Second side value of triangle\n"))
s3 = int(input("Enter the third side value of triangle\n"))

if s1 == s2 and s2 == s3:
    print("It is equilateral triangle")

elif s1 == s2 or s1 == s3 or s2 ==s3:
    print("It is isosceles triangle ")

else:
    print("it is a scalene")