dict1 = {"name":"Kimora", "grade":12,"school":"codingal"}
print(dict1)

print(len(dict1))
print(type(dict1))

print(dict1["school"])
print(dict1.values())
print(dict1.items())

dict1["rollno"]=2
print(dict1)

dict1.popitem()
print(dict1)

dict1.clear()
print(dict1)

del dict1
print(dict1)