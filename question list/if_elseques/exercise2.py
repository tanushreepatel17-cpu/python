
#unit           price 
# 100 unit      no charge 
# #200unit      5rs per unit
# #300unit      10rs per 

unit = int(input("enter unit: "))

if unit <=100:
    print("no charge")
elif 100 < unit <=200:
    total = (unit - 100) *5
    print(f"unit is {unit} so the total amount {total}")
elif unit > 200:
    total = (100*5) +(unit -200)*10
    print(f"unit is {unit} so the total amount {total}")
else:
    print("enter unit")