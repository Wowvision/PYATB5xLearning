#Encapsulation
from NOV.ex_30112024_OOPS.Lab_115_Ecapsulation_ft import object_ref


#hide the data members(class variables, instance variables)
# by using only the methods .

class Car:

    def __init__(self):
        self.password = "pramod"       #public variable
        self.__password_secure = "Pass123"      #private variable

    def change_password(self):
        print(self.password)

object_ref = Car()
print(object_ref.password)
print(object_ref.__password_secure)   # 'Car' object has no attribute '__password_secure'.
                                       # Did you mean: '_Car__password_secure' we cannot
                                       #access outside 