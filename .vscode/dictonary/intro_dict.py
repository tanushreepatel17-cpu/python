#dictoinary 
#dictonary is key value pair
d = {}
print(type(d))
d = {1:10, 2:20, 3:30, 4:40}
print(type(d))

#mutable : you can change add or remove elements
#we can not change keys but we can change values

#ordered : dectonary follows insertion order, key are in place of indexing here indexing is not allowed

#duplicate: key must be unique but you can have duplicate in value
d = {1:10, 2:20, 3:10, 4:20}
print(d)

#Hatrogenious : a dictonary can store different type of keys and values. like integers, string, lists. tupleor even another dictonary
d = {1:"hello", 2:"tanu", 3:"hello"}
print(d)

#print value in dict
d = {10:100, 20:200, 30:300, 40:400}
print(d[20])
print(d[40])     

#update the vaslue
d = {10:100, 20:200, 30:300, 40:400}
d[10] = 1000
print(d) 

#we can create the value
d = {10:100, 20:200, 30:300, 40:400}
d.update({50:500})
d[10] = 100  #updating the value
d[50] = 500 #creating the value
print(d)


#traversing in dict
#we can traverse keys and values at the same time
d = {10:100, 20:200, 30:300, 40:400}

for i in d:
    print(i)

for i in d:
    print(d[i])

for i in d.values():
    print(i)