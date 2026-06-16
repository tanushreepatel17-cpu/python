s1 = int(input("enter s1: "))
s2 = int(input("enter s2: "))
s3 = int(input("enter s3: "))
if s1 + s2 > s3 and s2 + s3 > s1 and s1 + s3 > s2:
    print("triangle is possible")
else:
    print("triangle is not possible")