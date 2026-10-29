row = int(input("enter row size: "))
for i in range(1,row+1):
    for j in range(1,i+1):
        if j == 1 or i == row or j == i :# j == 1 (column one) or i==row (the last row assuming total count of row) or j == i (row and column are equal)
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()