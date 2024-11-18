# Program to find area of circle given the radius
# area=3.14*r^2

#Login building formula

# || Step1 ||
# Figure out the input and output
#input ->r datatype -> float
# pi = 3.14
#power -> pow or **
#float ->area print ->area

# Rough logic
#area = 3.14 * pow(r,2)

# Step 3

radius = float(input("Enter the radius of circle\n"))
print(radius)

area = 3.1438448381 * (radius**2)

print("the area of circle is :" , area)
print(f"the area of circle is ->  {area :.3f}")     #both are same

import math

print(math.pi)
print(math.sin(90))
print(math.cos(90))
print(math.tan(90))
