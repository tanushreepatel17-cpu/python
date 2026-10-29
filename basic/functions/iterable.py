#iterables = An object/collection that can return its elements one at a time allowing it to be iterable in a loop
#example: list are iterable
numbers = [1,2,3,4,5]
for number in numbers:
    print(number)

#example: you can reverse a function
numbers = [1,2,3,4,5]
for number in reversed(numbers):
    print(number, end=" ")


#tuple are iterable
numbers = (1,2,3,4,5)
for number in numbers:
    print(number)


#sets are iterable
#set object is not reversible
fruit = {"apple", "orange", "banana", "coconut"}
for fruit in (fruit):
    print(fruit)


#dectonary are iterable
name= "Bro Code"
for character in name:
    print(character, end=" ")

#another example

my_dictonary = {"A":1, "B":2, "C":3}
for key,value in my_dictonary.items():
    print(f"{key}={value}")