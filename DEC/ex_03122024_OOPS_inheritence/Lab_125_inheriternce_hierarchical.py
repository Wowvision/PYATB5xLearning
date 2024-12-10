class Father:
    def BHK1(self):
        print("1 BHK")

class Shubham(Father):

    def BHK2(self):
        print("2 BHK")

class Amit(Father):

    def BHK3(self):
        print("3 BHK")

class Lucky(Father):

    def no_House(self):
        print("No house")

s_ref = Shubham()
s_ref.BHK1()
s_ref.BHK2()

a_ref = Amit()
a_ref.BHK1()
a_ref.BHK3()

l_ref = Lucky()
l_ref.BHK1()
l_ref.no_House()