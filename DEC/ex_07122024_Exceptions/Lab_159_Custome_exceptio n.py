# Custome exception


class LowBalancecustomeexception(Exception):
    def __init__(self, messeage):
        self.messeage = messeage
        super().__init__(messeage)


Balance = 100
Widrwal = int(input("Enter the ammount to be widrawl"))
if Widrwal > Balance:
    raise LowBalancecustomeexception("Balance is low")
else:
      print("Remaining balnce", (Balance-Widrwal))
