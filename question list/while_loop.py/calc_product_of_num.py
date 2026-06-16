#by using for loop 

num = 1
for i in range(1,6):
    num *= i
print(f"product of number is {num}")

#by using while loop

num = 1
product = 1
while num <= 5:
    product *= num
    num += 1
print(f"product of number is {product}")

