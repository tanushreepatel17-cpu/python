#list comprehension = A concise way create list in python
#                     compact and easier to read than traditional loops
#                     [expression for value in iterble if condition]

#printing first letter of list
fruits = ["apple", "orange", "banana", "coconut"]
fruit_chars = [fruit[0] for fruit in fruits]
print(fruit_chars)


 #exercise

numbers = [1, -2,3,-4,5,-6,8,-7]
possitive_nums = [num for num in numbers if num >=0]
negative_nums = [num for num in numbers if num <0]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 == 1]

print(even_nums)


#exercise

grades = [85, 42, 79, 99, 56, 61, 30]
passing_grades = [grade for grade in grades if grade >= 60]
print(passing_grades)
