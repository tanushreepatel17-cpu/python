principal = 0
rate = 0
time = 0
while True:
    principal = float(input("enter principal: "))
    if principal < 0:
        print("principal can not be zero")
    else:
        break # exit the loop
while True:#true is a boolean value that is always true, so the condition never becomes false by itself.
    rate = float(input("enter rate: "))
    if rate < 0:
        print("rate can not be less then zero")
    else:
        break #exit the loop
while True:
    time = int(input("enter time"))
    if time < 0:
        print("time can not be less then zero")
    else:
        break #exit the loop
total = principal * pow((1 + rate)/100,time)
print(f"balance after {time} year: ${total:.2f}")