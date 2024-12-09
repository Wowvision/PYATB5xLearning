a = 10

class person:
    b = 11   #instance variable

    def print_info(self):
        c = 20   # local variable we can access directly
        #print(self.c)  #can be access directly
        print(c)
        print(self.b) #instance variable can not access directly
        global a
        #a = "Hello"
        print(a)

object_ref = person()
object_ref.print_info()
