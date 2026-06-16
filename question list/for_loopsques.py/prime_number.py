#check prime num or not
num = int(input("enter any number: "))
for i in range(2,num):
    if num % i == 0:
        print(f"{num} is not prime")
        break
else:
    print(f"{num} is prime")