row = int(input("enter row size for pattern: "))
for i in range(1,row+1): #upper part of diamond
    for j in range(row-i):
        print(" ", end=" ")
    for k in range(2 * i - 1):
        print("*", end=" ")
    print()

for i in range(row-1,0,-1): #lower part of diamond
    for j in range(row-i):
        print(" ", end=" ")
    for k in range(1,2 * i):
        print("*", end=" ")
    print()