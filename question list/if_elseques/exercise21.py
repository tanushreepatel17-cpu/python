n1 = int(input(" enter num1:  "))
n2 = int(input("enter num2: "))
n3 = int(input("enter num3: "))
if (n1 > n2 and n1 < n3) or (n1 < n2 and n1 > n3):
    print("second largest num: ",n1)
elif (n2 > n1 and n2 < n3) or (n2 < n1 and n2 > n3):
    print("second largest num: ",n2)
else:
    print("second largest num: ",n3)