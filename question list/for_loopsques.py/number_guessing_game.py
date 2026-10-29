#create number guessing game using loops
import random
secret_number = random.randrange(1,11)
print(secret_number) # if i write print(secret_number) so the secret_number will visible  
                     # if i dont write ........ so it cannot visible
while True:
    guess = int(input("enter your numbr between 1 to 11: "))
    if guess == secret_number:
        print("you guessed a correct number!")
    elif guess > secret_number:
        print("number is too high! ")
    else:
        print("number is too low! ") 