#inheritance = Allows a class to inherit  attributes and methods from another class 
#            helps with code reusability and reduces complexity of a program 

class Animal:
    def __init__(self, name): #defining a constructor
        self.name = name
        self.is_alive = True
    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal): #dog class is inherit from animal class
    def speak(self):
        print("WOOF! ")
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is asleep")
class Cat(Animal):
    def speak(self):
        print("meow!! ")

class Mouse(Animal):
    def speak(self):
        print("squece! ")

dog = Dog("Scooby ")
cat = Cat("rossy ")
mouse = Mouse("vicky")

print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()

mouse.speak()
cat.speak()
dog.speak()                 
