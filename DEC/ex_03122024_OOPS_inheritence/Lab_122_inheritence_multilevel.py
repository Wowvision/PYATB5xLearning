#Multilevel inheritence

#GF -> F -> Child

class Grandfather:
    gold = "2kg"

    def BHK2(self):
        print("2 BHK")

class Father(Grandfather):
    Diamond = "Diamond"

    def BHK3(self):
        print("3 BHK")

class Son(Father):
    btc = "1 btc"

    def BHK1(self):
        print("1 BHK")

s_ref = Son()
s_ref.BHK1()
s_ref.BHK2()
s_ref.BHK3()
print(s_ref.gold)
print(s_ref.Diamond)
print((s_ref.btc))

f = Father()
#print(f.btc)  # not possible
print(f.gold)