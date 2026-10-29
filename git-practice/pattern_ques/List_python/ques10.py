#Combine Two Lists
List_A= ["Physics", "Chemistry"]
List_B= ["Maths", "Biology"]

#metod 1 using + operator
combined_list = List_A + List_B
print(f"combined_list: {combined_list}")

#method two using extend method
List_A.extend(List_B)
print(f"combined_list:{List_A}")