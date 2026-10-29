#Count Even and Odd Numbers
number = [10, 21, 4, 45, 66, 93, 11]
even_count = 0
odd_count = 0
for num in number:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(f"even count: {even_count}")
print(f"odd count: {odd_count}")