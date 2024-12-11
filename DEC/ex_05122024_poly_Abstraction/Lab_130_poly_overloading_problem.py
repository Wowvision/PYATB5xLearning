#Method overloading:- Method overloading is not possible in python tradionally becasue
#interpretor will confused in same method name  Sum

class Calc:

    def sum(self,a ,b ):
        return a + b

    def sum(self, a,b,c):
        return a + b+ c

calc_ref = Calc()
result = calc_ref.sum(1,2)
print(result)