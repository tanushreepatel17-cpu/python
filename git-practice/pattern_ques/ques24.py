 # Number pyramid pattern

row = int(input("enter row size: ")) #outer loop for row
for i in range(1,row+1):
    for j in range(row - i):# inner looop for space
        print(" ", end=" ")
    for k in range(1 , i + 1):# inner loop for number printing
        print(k , end=" ")
    for l in range(i-1, 0, -1):#inner loop for reverse number
        print(l, end=" ")
    print()