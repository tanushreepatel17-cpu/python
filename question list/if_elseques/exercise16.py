ser = int(input("enter your service: "))
sel = int(input("enter your selery: "))
if ser > 10:
    b = 10/100*sel
    print(b)
elif ser >=6 and ser<= 10:
    b = 8/100*sel
    print(b)
elif ser <= 5:
    b = 5/100*sel
    print(b)
else: 
    print("please enter the details")