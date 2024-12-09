class Home:

    def __init__(self):
        self.public_var = "Father"
        self.__private_var = "Children"

    def Mom(self):
        print(self.__private_var)
        self.__wife()      #can access publically

    def __wife(self):
        self.__wife()

home_ref = Home()
home_ref.Mom()
print(home_ref.public_var)#can access because public in nature
home_ref.__wife  #  not access directly
#print(home_ref.__private_var)  #Home' object has no attribute '__private_var'.
                                # Did you mean: '_Home__private_var'?
