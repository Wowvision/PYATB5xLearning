# Static method

class O:

    @staticmethod
    def sum(a,b):
        return a+b           #Static on nature

    def sub(self,a,b):
        return a-b           #Non Static in nature

O_ref = O()
print(O_ref.sub(2,3))

print(O.sum(2,4))
