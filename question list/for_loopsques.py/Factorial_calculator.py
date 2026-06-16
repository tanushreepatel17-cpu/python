#compute the factorial of a number using a while loop
num = int(input("enter any number: "))
factorial = 1 #factorial can not be zero

while num > 0:
    factorial *= num
    num -= 1

print(f"factorial is: {factorial}")
