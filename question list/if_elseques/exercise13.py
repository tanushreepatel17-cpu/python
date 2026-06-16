age1 = int(input("enter age of person1: "))
age2 = int(input("enter age of person2: "))
age3 = int(input("enter age of person3: "))
age4 = int(input("enter age of person4: "))

if age1>age2 and age1>age3 and age1>age4:
    print("person1 is older")
elif age2>age1 and age2>age3 and age2>age4:
    print("person2 is greater")
elif age3>age1 and age3>age2 and age3>age4:
    print("person3 is older")
else:
    print("person4 is older")
                