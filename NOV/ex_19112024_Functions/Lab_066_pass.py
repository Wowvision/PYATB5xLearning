# def first_part_last_name():
#     pass
# print("hello")
#
# first_part_last_name()


def greet_to_all_of_you():
    print("hello , Everyone")
    pass

#Function within function
def greet():
    print("hello")
    greet_to_all_of_you()

greet()
