class A:
    def methodA(self):
        return "Method A"

class B(A):

    def methodB(self):
        return "Method B"

class C(A):

    def methodC(self):
        return "Method C"

class D(B,C):

    def methodD(self):
        return "Method D"

d_ref = D()
print(d_ref.methodA())
print(d_ref.methodB())
print(d_ref.methodC())
print(d_ref.methodD())

