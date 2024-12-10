class Father:

    def father_money(self):
        return 5
    def home(self):
        return "this is father home"

class Mother:

    def mother_money(self):
        return 3

    def home(self):
        return "This is mother home"

# class Son(Father, Mother):   # python will be called first parent class
# in child class
class Son(Mother, Father):  #Multiple inheritence

    def print_info(self):
        print("Son")

s_ref = Son()
print(s_ref.mother_money())
print(s_ref.father_money())
print(s_ref.home())