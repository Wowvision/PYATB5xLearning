my_list =[1,2,3]

#Indexing
print("Element at the index 0:" , my_list[0])
print("Element at the index 1:" , my_list[1])
print("Element at the index 2:" , my_list[2])

#append():- Append object to end of the list

my_list.append(4)
my_list.append(5)
print(my_list)


#extend() :- append a new list

my_list.extend([7,8,9])
print(my_list)

#insert() :- Add new value as per index

my_list.insert(1,"Goel")
my_list.insert(2,"Shubham" )
print(my_list)

my_list[1]="mannu"
print(my_list)

#remore()
my_list.remove("mannu")
print(my_list)

print("-------------------------------")
print("-------------------------------")


#copy of list
my_copy_list=my_list.copy()
print(my_list)
print(my_copy_list)

my_copy_list.remove("Shubham")

#Sort
my_copy_list.sort()
print(my_copy_list)


