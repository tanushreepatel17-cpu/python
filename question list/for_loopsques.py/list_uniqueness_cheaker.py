#ckeck if all elements in list are umnique. if a duplicate is found, exit the loop and print the duplicate.

items = ["apple", "banana","orange","apple","mango"]

unique_item = set() #A set is a collection of unique values.
                    #it does not allow duplicates.
for item in items:
    if item in unique_item:
        print("dupklicate item is", item)
        break
    unique_item.add(item)