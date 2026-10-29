#Add New Item After a Specified Item
list= [10, 20, 30, 40, 50]
target = 30
new_val = 35
index = list.index(target)
list.insert(index + 1,new_val)
print(f" updated list: {list}")