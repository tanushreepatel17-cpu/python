#Remove All Occurrences of a Specific Item

list= [5, 20, 15, 20, 25, 50, 20]
target = 20
#filter the list using a comprehension
cleaned_list = [x for x in list if x != target]

print(f"cleaned_list: {cleaned_list}")