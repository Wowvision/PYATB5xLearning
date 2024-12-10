from DEC.ex_03122024_OOPS_inheritence.Lab_120_inheritence_single import Father


class Parent:
    Gold = "2kg"

    def __init__(self):
        print("DC- parent")

    def BHK2(self):
        print("2 BHK")

class Child(Parent):
    Diamond = "diamond"

    def __init__(self):
        print("DC -> child")

    def BHK3(self):
        print("3 BHK")

child_ref = Child()
print(child_ref.Gold)
child_ref.BHK2()

Parent_ref = Parent()
Parent_ref.BHK2()
#Parent_ref.BHK3  # not able to access