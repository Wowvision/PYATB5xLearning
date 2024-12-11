#Method overloading:- Method overloading is not possible in python tradionally becasue
#interpretor will confused in same method name  Sum

class Calc:

    def sum(self,a ,b ):
        return a + b

    def sum(self, a,b,c=1):   #By default we need to define the value of C so it will
                                #autometiccaly picked second SUM method which has three arguments
                                #a,b,c
        return a + b+ c

calc_ref = Calc()
result = calc_ref.sum(1,2)
print(result)