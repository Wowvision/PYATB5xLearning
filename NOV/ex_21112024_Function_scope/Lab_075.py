pb_global_p = 30    # acting as a global variable

def my_function():
    pb_local_p=20    #acting as a local variable because its define under function
    print(pb_local_p)
    print(pb_global_p)

# print(pb_local_p)    # not possible to access because local with in function
my_function()
print(pb_global_p)  #allowed because it is global variable
