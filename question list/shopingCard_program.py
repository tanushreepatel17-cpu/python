#shoping card program

food = []
prices = []
total = 0

while True:
    foods= input("Enter a food to buy (q to quit):")
    if foods.lower()== "q":
        break
    else:
        price= float(input(f"Enter the price of a {food}: $"))
        food.append(food)
        prices.append(price)
print("_____YOUR CART_____")

for food in foods:
    print(food,end=" ")

for price in prices:
    total += price
print()
print(f"your totalis: ${total}")    