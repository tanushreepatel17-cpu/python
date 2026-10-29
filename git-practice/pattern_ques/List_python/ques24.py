#Replace List’s Item with New Value if Found
list= [5, 10, 15, 20, 25]
find= 20
replacement= 200

if find in list:
    index= list.index(find) 
    list[index] = replacement
print(f"modified list: {list}")