number = [12,45,8,67,23]
largest = number[0]
second_largest = number[0]

for num in number:
    if num > largest:
        largest = num
        second_largest = largest
    elif num > second_largest and num != largest:
        second_largest = num
print("second_largest number: ",second_largest)