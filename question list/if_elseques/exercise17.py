na = 0
d = 0
mp = int(input("enter markedprice: "))
if mp > 10000:
    d = 20/100*mp
elif mp > 7000 and mp <= 10000:
    d = 15/100*mp
else:
    d = 10/100*mp
na = (mp - d)
print("net ammount: ",na)
print("discount is: ",d )