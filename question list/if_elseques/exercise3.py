per = int(input("enter your percentage: "))

if per > 90:
    print("Grade: A")
elif 80 < per <= 90:
    print("Grade: B")
elif 60 <= per <=80:
    print("Grade: C")
else:
    print("Grade: D")