#python dictonary methods are function used to add, remove ,access, or modify key-values pair
s = {"name":"tanushree", "Age": 19, "branches":"AIMl"}

#1. get()
#gets the value of a key.
s = {"name":"tanushree", "Age": 19, "branches":"AIMl"}
print(s.get("name"))

#if key dosent exist: it returns none
print(s.get("marks"))

#you can also give a default value:
print(s.get("marks",10))

#2. keys(): returns all keys.
print(s.keys())


#3. values(): returns all values.
print(s.values())


#4. item():returns key-value pair **very commonly used with loop
print(s.items())


#5. update(): Add new key-value pair or changes existing values.
s.update({"age":20})
print(s)


#6. pop(): removes a specific key and returns its values
print(s.pop("age"))
print(s.pop("name"))


#7. popitem(): Removes the last inserted key-value pair.
print(s.popitem())


#8. clear(): Remove everything from the dictonary.
print(s.clear()) #it doesnt delete the dict itself it just make it empty.


#9. copy(): Create a cpoy of a dictonary.
s = {"name":"tanushree", "Age": 19, "branches":"AIMl"}
s2 = s.copy() #now s2 has the same data as s.
print(s2)


capitals ={" USA": "washingten D.C",
           "India": "new Delhi",
             "china":"beijing",
               "Russia": "moscow"}

print(capitals.get("japan"))

if capitals.get("Russia"):
    print("That capital exist")
else:
    print("that capital doesn;t exist")

capitals.update({"germany": "be rlin"})
print(capitals)

keys = capitals.keys()
print(keys)
for key in capitals.keys():
    print(key)

values = capitals.values()
for value in capitals.values():
    print(value)

