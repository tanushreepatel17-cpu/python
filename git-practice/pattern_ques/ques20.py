#Hollow Diamond pattern 

row = int(input("enter row size: "))
for i in range(1,row + 1):
    for j in range(row - i):
        print(" ", end=" ")

    for k in range(1, 2 * i):
        if k == 1 or k == 2 * i - 1:
            print("*" ,end=" ")

        else:
            print(" ", end=" ")
    print()

for i in range(row-1, 0, -1):
    for j in range(row - i):
        print(" ", end=" ")

    for k in range(1, 2 * i):
        if k == 1 or k == 2 * i - 1:
            print("*" ,end=" ")

        else:
            print(" ", end=" ")
    print()
    