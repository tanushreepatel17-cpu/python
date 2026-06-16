#keep aski ng the user for input until they enter a number between 1 and 10
num = int(input("Enter any number b/t 1 to 10: "))

while True:
    num = int(input("Enter any number b/t 1 to 10: "))

    if 1 <= num <= 10:
        print("Thankyou")
        break
    else:
        print("invalid number, please try again!")
        