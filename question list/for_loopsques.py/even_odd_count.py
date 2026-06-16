even_count = 0
odd_count = 0
for i in range(1,101):
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(f"even numbers are: {even_count}")
print(f"odd number are: {odd_count}")