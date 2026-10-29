#Random number generation in python {method}
import random
low = 1
high= 100
options = ("rock", "paper", "scissors")
cards =["2", "3", "4","5", "6", "7", "8", "9", "10" "J", "K", "Q", "A"]

#random.randint(low,high): this method will return a random integer between low and high (both inclusive number = random.randint(low,high)
number = random.randint(low,high)
print(number)

#random.random(): this method returns a random floating point number between 0.0 and 1.1
number =random.random()
print(number)

#random.choice: 
# this is useful for picking a single random element from a collection, such as a list or a tuple
option = random.choice(options)
print(option)

#random.suffle: this method rearranges the order of elements within a mutable sequences, like a list, effectively
random.shuffle(cards)
print(cards)