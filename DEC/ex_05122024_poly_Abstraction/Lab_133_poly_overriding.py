from DEC.ex_03122024_OOPS_inheritence.Lab_120_inheritence_single import Father


class Parent:

    def home(self):
        print("2BHK")

class Son(Parent):

    def home(self):    #overriden same method in class
        print("3BHK")

s_ref = Son()
s_ref.home()