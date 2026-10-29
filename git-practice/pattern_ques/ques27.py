#alphabel right angled triangle pattern

row = int(input("enter row size: "))
for i in range(1,row+1):
    for j in range(1,i+1):
        print(chr(64+j), end=" ")
    print()