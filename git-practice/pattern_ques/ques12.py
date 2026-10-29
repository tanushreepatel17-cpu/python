row = int(input("enter the row size for the pattern: "))
for i in range(1,row+1):
    for j in range(1,row-i+1):
        print("*", end=" ")
    print()