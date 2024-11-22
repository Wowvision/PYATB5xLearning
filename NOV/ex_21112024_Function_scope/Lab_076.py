public_toilet = "pb"

def home():
    private_toilet = "pt"
    print(private_toilet)
    print(public_toilet)

def strange():
    print(public_toilet)
    #print(private_toilet)   # not allwed in another function due to local its scope in only
    # under function


print(public_toilet)   # allowed because it is global variable
# print(private_toilet) not available due to local variable