#union
set1 ={1,2,3}
set2 ={4,5,6}
result = set1.union(set2)
print(result)

#intersection
set1 ={1,2,3,4,5,6}
set2 ={4,5,6,7,8}
result = set1.intersection(set2)
print(result)

result = set1.difference(set2)
print(result)
result = set2.difference(set1)
print(result)
