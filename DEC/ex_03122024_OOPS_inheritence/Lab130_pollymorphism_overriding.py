class Father:
    def home(self):
        print("1 BHK")

class Shubham(Father):
    def home(self):
        print("2 BHK")

s_ref = Shubham()
s_ref.home()

f_ref = Father()
f_ref.home()