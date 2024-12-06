class Calculator:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

Object_ref = Calculator(4,5)

# output = Object_ref.sum()
# output1= Object_ref.sub()
# output2= Object_ref.mul()
# output3= Object_ref.div()
#
# print(output,output1,output2,output3)

Object_ref.sum()

