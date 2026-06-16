a = int(input("enter num of working days: "))
b = int(input("enter num of absent days: "))
per = ((a+b)/2)*100
if per > 75:
    print("student will not be able to sit in exam")
else:
    print("student will be able to sit in exam")