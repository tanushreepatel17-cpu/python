#Butterfly Pattern 
row = int(input("enter row size: "))
for i in range(1, row + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    for j in range(2 * (row - i)):# for printing space between rows
        print(" ",end=" ")
    for j in range(1, i + 1):# for printing* right side
        print("*", end=" ")
    print()

for i in range(row, 0, -1):
    for j in range(1,i+1):
        print("*", end=" ")
    for j in range(2 * (row - i)):# for printing space between rows
        print(" ",end=" ")
    for j in range(1,i+1):# for printing* left side
        print("*", end=" ")
    print()