row = int(input("enter row size: "))
for i in range(row ,0 , -1):
    for j in range(1, i + 1):
        if j == 1 or i == row or i==j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()