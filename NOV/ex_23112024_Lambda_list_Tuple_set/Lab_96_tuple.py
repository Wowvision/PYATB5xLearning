cities =("india","Australia","canada","united states")
print("paris" in cities)
print("india" in cities)

#how to append in tuple-first convert into list then apped
t = (12,14,189)

my_list = list(t)
my_list.append(4)
t = tuple(my_list)
print(t)
