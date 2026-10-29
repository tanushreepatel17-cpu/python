#count frequency of each character in a string
a = input("enter your name: ") 
d = {}
for char in a.upper():
    if char in d:
        d[char] += 1
    else:
        d[char] = 1
for char in d:
    print(f"{char} : {d[char]}")
