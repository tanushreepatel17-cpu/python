#*args = allows you to pass multiple non-key arguments
#**kwargs = allow you to pass multiple keyword- arguments
#          unpacking operator

#*args
def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,2,3))

#example
def display_name(*args):
    for arg in args:
        print(arg, end=" ")
display_name("Dr.", "sponbob", "harold", "squarepants",)

#**kwargs 
def print_address(**kwargs):
    for key , value in kwargs.items():
        print(f"{key}: {value}")
print_address(street="123 Fake st.",
              apt="100",
              city="detroit",
              state="MI",
              Zip="54321")


#args and kwargs together
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('state')},{kwargs.get('zip')}")
shipping_label("Dr.", "Spongebob","squarepants",
               street="123 Fake st.",
               pobox="po box #1001",
               city= "jabalpur", 
               state= "MP",
               zip= "54321")   