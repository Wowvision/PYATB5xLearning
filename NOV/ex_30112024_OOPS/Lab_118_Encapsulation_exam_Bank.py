class Bank:


    def __init__(self, account_number, acc_balance):
        self.balance = acc_balance
        self.__number = account_number

    def check_balance(self):
        print(self.balance)

    def public_method(self):
        print(self.__internal_private_method())   #public method can be access private method
                                                  # and variable called encapsulation

    def deposit(self, amount):
        self.balance = self.balance + amount

    def show_acc_number(self, isauth):
        if(isauth == True):
         print(self.__number)
        else:
         print("Not allowed!")

    def __internal_private_method(self):
        print("Private menthod, can only be accessed in class")


icici_ref = Bank("9876543212", 100)
icici_ref.deposit(100)
icici_ref.check_balance()
print(icici_ref.balance)  # accesible because it public
#print(icici_ref.__number)  # not allowed its allowed with the help of method line 14
#icici_ref.show_acc_number(False)
icici_ref.show_acc_number(True)
