#introduction of set
s = {1,2,3,4} #it indicates by curly bracket
              #sets are mutable, we can change the value
              #sets cannot have duplicate value, every element will be unique
              #sets dont have any index  value, its unordered thing
              #sets are semi hetrogenious it can store some data type like string ,number,tuple but not everything 
              # vin set the is stored in the form of hashing
#traverse in sets 
# a set cannot be traversed using the index value cause it is unordered and has no index
a = {1,2,3,8,9,4,5}

for i in a:
    print(i)

#set method
a = {1,2,3,8,9,4,5}
a.remove(3)
print(a)

a.pop()
print(a)

a.clear()
print(a)
# union of a and b
a = {1,2,3,4,5}
b = {4,5,6,7,8}
s = a|b
print(s)

#intersection of a and b
a = {1,2,3,4,5}
b = {4,5,6,7,8}
s = a&b
print(s)

#symatric difference of a and b
a = {1,2,3,4,5}
b = {4,5,6,7,8}
s = a^b
print(s)
 
