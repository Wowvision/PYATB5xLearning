#Method overloading:- Method overloading is not possible in python tradionally becasue
#interpretor will confused in same method name  Sum

class Calc:

    def sum(self,*args ):
        for i in args:
            print(i)

calc_ref = Calc()
calc_ref.sum(1)
print("---------")
calc_ref.sum(1,2)
print("---------")
calc_ref.sum(1,2,3)