#Find the Most Frequent Element
def find_mode(arr):
    frequency = {}

    for item in arr:
        frequency[item] = frequency.get(item,0)+1
        
#find the key with the maximum value
    mode = max(frequency, key=frequency.get)
    return mode

data = [1,3,3,2,1,1,4,3,3]
result = find_mode(data)
print(result)