#How to create a class

#Single inheritence -> You will use 85% single inheritence in API, Web automation


class Father:
    key = "2BHK"

    def Car(self):
        print("Father has a car -> Alto")
        print(self.key)


class Son(Father):  #Single inheritence
    key = "3BHK"

    def Suv(self):
        print("Son has a SUV car MG hector-> black")
        print(self.key)

Father_ref = Father()
Father_ref.Car()

Son_ref = Son()
Son_ref.Car()