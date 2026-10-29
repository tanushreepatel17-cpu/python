#Floyd's Triangle Pattern 

row = int(input("enter row size: "))
num = 1
for i in range(1,row+1):
    for j in range(1,i+1):
        print(num , end=" ")
        num +=1
    print()