# Concatenate Two Lists Index-wise
list1= ["Py", "is", "awes"]
list2= ["thon", " ", "ome"]

res = [i+j for i,j in zip(list1,list2)]

print(f"merged: {res}")