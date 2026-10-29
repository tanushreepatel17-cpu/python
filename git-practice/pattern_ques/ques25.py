

row = int(input("enter row size: "))
for i in range(row,0,-1):
    for j in range(row - i):
        print(" ", end=" ")
    for k in range(1 , i + 1):
        print(k , end=" ")
    for l in range(i-1, 0, -1):
        print(l, end=" ")
    print()