#Number pyramid pattern 
row = int(input("enter row size: "))
for i in range(1,row+1):
    for j in range(row-i):
        print(" ", end=" ")
    for k in range(1,2*i):
        print(k, end=" ")
    print()
