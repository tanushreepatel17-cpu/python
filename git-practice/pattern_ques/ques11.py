n = 5
for i in range(1,6):
    for j in range(i):
        print(" ", end=" ")
    for j in range( 2 * (n-i) + 1):
        print("*",end=" ")
    print()
    