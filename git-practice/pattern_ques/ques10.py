n = 7
for i in range(1,8):
    for j in range(i):
        print(" ", end="")
    for j in range(n-i):
        print("*", end=" ")
    print()