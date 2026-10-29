    #concession stand program
menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips":1.00,
        "pretzel":3.50,
        "soda": 3.00,
        "lemonade":4.25}
cart = []
    
total = 0            

print("---------menu---------")
for key,value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("-----------------------")

#we would like to user for some input that what should they want to buy
while True:
    food = input("select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
print("----------yuor item----------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ") 

#lets calculate the total

print()
print(f"total is: ${total: 2f}")



 