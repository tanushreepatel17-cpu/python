#Turn Every Item of a List into its Square (List Comprehension)
#The syntax for a list comprehension is [expression for item in list].
#Your expression here should be x * x.

list= [1, 2, 3, 4, 5]

squared_list = [x*x for x in list]
print(f"squared_list: {squared_list}")