value=float(input("enter the numbeerr: "))
unit= input("enter the cm or m: ")

if unit == "m":
    m = value/100
    print(f"value of metre is {m}")

elif unit == "cm":
    cm = value*10
    print(f"value of cm is {cm}")

else:
    print("invalid unit")