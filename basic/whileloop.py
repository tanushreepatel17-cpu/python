#while loop = execution some code while condition remains true

food = input("enter a food you like ('q to quit):")

while not food == 'q':
    print(f"you like {food}")
    food = input("enter a food you like ('q to quit):")
print("bye")

#print any number between 1 to 10
num = int(input("enter any number between 1 to 10: "))
while num < 0 or num>10:
    print(f"{num} is not valid")
    num = int(input("enter any number between 1 to 10: "))
print(f"your number is {num}")

#print age using while loop 
age = int(input("enter your age: "))
while age<0:
    print("age cant be negative") 
    age = int(input("enter your age: "))
print(f"you are {age} year old")
