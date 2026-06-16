per = int(input("enter your percentage: "))
if per > 80:
    print("grade A+")

elif per > 60 and per <= 80:
    print("grade A")

elif per > 50 and per <= 60:
    print("grade B+")

elif per > 45 and per <= 50:
    print("grade B")

elif per > 25 and per <=45:
    print("grade c")

else:
    print("grade D")