class XYZ:
    def f1(self):
        try:
            a= int(input("Enter the number"))
        except Exception as e:
            print("Only int value to be enter")
        else:
            print(a)
        finally:
            print("I will be always executed")
xyz_ref = XYZ()
xyz_ref.f1()
