#weight conversion 
weight = int(input("enter the weight: "))
unit = input("enter the unit kg/lb: ")
if unit == "kg":
    weight = round(weight * 2.205)
    print(f"the weight in pounds is {weight}")
elif unit == "lb":
    weight = round(weight / 2.205)
    print(f"the weight in kilograms is {weight}")
else:
    print("invalid unit")