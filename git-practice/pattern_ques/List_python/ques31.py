def specific_concat(lst1,lst2):
  return [x + y for x in lst1 for y in lst2]
  
L1= ["Hello ", "Take "]
L2= ["Dear", "Sir"]
result = specific_concat(L1,L2)
print(result)
