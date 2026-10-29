row = int(input("enter row size: "))
for i in range(1,row+1):
    for j in range(row - i):
        print(" ",end=" ")
    for k in range(1, 2 * i):
        if k == 1 or k == 2 * i - 1 or i == row:# k == 1 first possition of the current row print*
                                            #k == 2*i-1 last possition print*
                                            #i == row ,last row print * in everywhare
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()