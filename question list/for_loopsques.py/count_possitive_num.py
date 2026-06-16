#given a list of number count how many are possitive

number = [1,-2,3,-4,5,6,-7,-8,9,10]
possitive_number_count = 0
for num in number:
    if num > 0:
        possitive_number_count += 1
        print(f"total possitive number is {possitive_number_count}")
        