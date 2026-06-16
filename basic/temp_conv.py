unit = input("is this temperature in c/f?:")
temp = float(input("enter the temp:"))

if unit == "c":
   temp = round((temp * 9/5) + 32,1)
   print(f"the temperature in fahrenheit is {temp}")

elif unit == "f":
    temp = round((temp -32) * 5/9)
    print(f"the temperature in celsius is {temp}")
else:
    print("invalid unit")

