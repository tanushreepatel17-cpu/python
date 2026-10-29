# Type Casting in Python
# Type casting is the process of converting a variable from one data type to another. In Python, you can use built-in functions to perform type casting.
# Example of type casting

name ="bro code"
age = 25
gpa = 3.2
is_student = True

print(type(name))
print(type(gpa))
print(type(age))
print(type(is_student))

#str() - converts a value to a string
#int() - converts a value to an integer
#float() - converts a value to a float
classmates = "" # if  you create an empty string, it will be considered as False when converted to a boolean
name = "bro code"
age = 25
gpa = 3.5
is_student = True

print(type(name))
print(float(age))
print(str(gpa))
print(bool(name))
print(bool(classmates))