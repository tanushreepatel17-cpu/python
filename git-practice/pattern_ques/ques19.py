#hollow inverted pyramid pattern in python


row = int(input("enter row size: "))
for i in range(row , 0, -1):
    
    for j in range(row - i):
        print(" ", end=" ")

    for k in range(1, 2 * i):
        if k == 1 or k == 2 * i -1 or i == row:
            print("*", end=" ")

        else:
            print(" ", end=" ")

    print() 