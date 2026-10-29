#format specifiers = {value: flags} format a value based on what flags are inserted

price1 = 3000.14159
price2 = -98700.65
price3 = 1200.34
#for 2 number print after(.)
print(f"price 1 is ${price1:.2f}")
print(f"price 1 is ${price2:.2f}")
print(f"price 1 is ${price3:.2f}")
#for 10 space
print(f"price 1 is ${price1:10}")
print(f"price 1 is ${price2:10}")
print(f"price 1 is ${price3:10}")
#for before
print(f"price 1 is ${price1:<10}")
print(f"price 1 is ${price2:<10}")
print(f"price 1 is ${price3:<10}")
#for back
print(f"price 1 is ${price1:>10}")
print(f"price 1 is ${price2:>10}")
print(f"price 1 is ${price3:>10}")
#for center
print(f"price 1 is ${price1:^10}")
print(f"price 1 is ${price2:^10}")
print(f"price 1 is ${price3:^10}")

print(f"price 1 is ${price1:+}")
print(f"price 1 is ${price2:+}")
print(f"price 1 is ${price3:+}")

print(f"price 1 is ${price1:,}")
print(f"price 1 is ${price2:,}")
print(f"price 1 is ${price3:,}")

print(f"price 1 is ${price1:+,.2f}")
print(f"price 1 is ${price2:+,.2f}")
print(f"price 1 is ${price3:+,.2f}")