input = "teeter"

for char in input:
    print(char)
    if input.count(char) == 1:
        print(f"char is {char}")
        break
    