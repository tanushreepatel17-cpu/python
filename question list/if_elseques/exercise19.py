s1 = int(input("enter side1: "))
s2 = int(input("enter side2: "))
s3 = int(input("enter side3: "))

if s1 == s2 and s1 == s3 and s2 == s3:
    print("triangle is equilatral")
elif (s1 == s2 and s1!=s3) or (s2 == s3 and s2!=s1) or (s3 == s1 and s3!=s2):
    print("triagle is isoscales")
else:
     s1 != s2 and s2 != s3 and s3 != s1
     print("triangle is scalence")