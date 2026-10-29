# invert alphabet right angle triangle pattern


row = int(input("enter row size: "))
for i in range(row, 0, -1):
    for j in range(1,i+1):
        print(chr(64+j), end=" ")
    print() 