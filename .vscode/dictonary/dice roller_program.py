# Function = A block of reusable code
#place () after the function name to invoke it


#def is used for define a function name
def happy_birthday(name, age):
    print(f" Happy birthday to {name}:")
    print(f" You are {age} years old! ")
    print("happy birthday to you!")
    print()

happy_birthday("tanushree", 20)
happy_birthday("anushree", 18)
happy_birthday("mahima", 20)

#another example:

def display_invoice(username, amount, due_date):
    print(f"hello {username}!")
    print(f"your bill of ${amount:2f} is due: {due_date}")
    print()
display_invoice("tanushree", 42.50, "01/01")

