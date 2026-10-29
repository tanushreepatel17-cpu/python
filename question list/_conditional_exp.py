#conditional expression = a one line shortcut for the if else statement (ternary operator)
# print or assign one of two value based on a condition
#x if condition else y
num = 10
a = 10
b = 15
age = 20
temp = 25   
user_role = "admin"
print("possitive" if num > 0 else "negative")
result = ("even" if num % 2 == 0 else "odd")
print(result)
#for printing greater number
max_num = print(a if a>b else b)

#for printing smaller number
mini_num = print(a if a<b else b)

#for printing age 
age = print("adult" if age>=18 else "child")

#for print temperature
temp = print("hot" if temp>=25 else "cold")

#for printing user role
access_level = print("full access" if user_role == "admin" else "limited access")