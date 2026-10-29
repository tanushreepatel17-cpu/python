list= [100, 50, 400,500]

#Change Element: Change the second element of a list to 200 and print the updated list.
list[1] = 200
print(f"updated (change): {list}")

#Append Element: Add 600 o the end of a list and print the new list.
list.append(600)
print(f"updated (append):{list}")

#Insert Element: Insert 300 at the third position (index 2) of a list and print the result
list.insert(2,300)
print(f"updated (insert): {list}")

#Remove Element (by value): Remove 600 from the list and print the list.
list.remove(600)
print(f"updated (remove 600): {list}")

#Remove Element (by index): Remove the element at index 0 from the list print the list.
list.pop(0)  #pop use on the "address" (index)
print(f"updated (remove index 0): {list}")