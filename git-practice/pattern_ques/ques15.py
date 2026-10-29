row = int(input("enter row size :"))
for i in range(1,row+1):
    for j in range(1,row+1):
        if i == row or i ==1:
            print("*", end=" ")
        elif j == row or j == 1:
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()