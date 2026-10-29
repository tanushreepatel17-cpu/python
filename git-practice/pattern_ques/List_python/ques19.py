#Remove Empty Strings from a List of Strings

list= ["Mike", "", "Emma", "Kelly", "", "Brad"]
target = ""
cleaned_list = [x for x in list if x != target ]
print(f"cleaned_list: {cleaned_list}")