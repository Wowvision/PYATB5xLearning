class Calculator:

    def __init__(self):
        print("Welcome to calculator")

    def sum(self, a,b):
        return a + b

    def sub(self, a,b):
        return a - b

    def mul(self, a,b):
        return a * b

    def div(self, a,b):
        return a / b

objref_calc = Calculator()

a= float(input("Enter the value of a"))
b= float(input("Enter the value of b"))

sum = objref_calc.sum(a,b)
sub = objref_calc.sub(a,b)
mul = objref_calc.mul(a,b)
div = objref_calc.div(a,b)

print("the sum is", sum,sub,mul,div)
