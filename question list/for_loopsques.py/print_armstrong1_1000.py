for num in range(1,1001):
    temp = num
    digits = len(str(num))
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10  # using floor division for removing the last digit of a number

    if total == num:
        print(num) 