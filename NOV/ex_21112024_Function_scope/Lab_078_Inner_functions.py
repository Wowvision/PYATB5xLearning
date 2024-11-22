def outer_function():
   var1=30

   def inner_function1():
       print(var1)

   def inner_function2():
       print(var1)

   inner_function1()
   inner_function1()
# print(var1)  ->not possible due to not allowed outside the function
outer_function()



