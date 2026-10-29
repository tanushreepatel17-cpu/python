#find graetest number peint its index too
l = [12, 14,55,100,98,120,65,78]
largest = l[0]
index = 0
for i in range (len(l)):
    if l[i] > largest:
        largest = l[i]
        index = i
print(f"your largest number is {largest} at index {index}") 
