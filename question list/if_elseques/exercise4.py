cost = int(input("enter cost of bike: "))

if cost > 100000:
    print("Tax: 15%")

elif 50000 < cost <=100000:
    print("Tax: 10%")

else:
    print("Tax: 5%")

