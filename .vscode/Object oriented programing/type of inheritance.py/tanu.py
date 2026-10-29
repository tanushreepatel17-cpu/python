#multiple inheritance = inherit from more than one parent class
#                        c(A,B)
#multilevel inheritance = inherit from a parent which inherit from another parent 
 #                       c(B) <- B(A) <- A 



#example of multiple inheritance
class Prey:#parent class
    def flee(self):
        print("this animal is fleeing")

class Predator:#parent class (there are two parent class in this)
    def hunt(self):
        print("this animal is hunting ")

class Rabbit(Prey):#child class
    pass

class Hawk(Predator):#child class
    pass

class Fish(Prey, Predator):#child class
    pass
rabbit = Rabbit()
hawk = Hawk()
fish = Fish()
rabbit.flee() #this csnnot hunt coz this is not bfrom predetor class
hawk.hunt() #this cannot flee coz this is not from prey class
fish.flee() #this canbe flee or hunt coz this from both class 
fish.hunt()
print("------------------------------")

#example of multilevel inheritance

class Animal:# Grand parent class

    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f"this {self.name} is eating")

    def sleep(self):
        print(f"this {self.name} is sleeping")

class Prey(Animal):#parent class
    def flee(self):
        print(f"this {self.name} is fleeing")

class Predator(Animal):#parent class (there are two parent class in this)
    def hunt(self):
        print(f"this {self.name} is hunting ")

class Rabbit(Prey):#child class
    pass

class Hawk(Predator):#child class
    pass

class Fish(Prey, Predator):#child class
    pass
rabbit = Rabbit("laxy")
hawk = Hawk("damen")
fish = Fish("alina")
rabbit.sleep() #this csnnot hunt coz this is not bfrom predetor class
rabbit.eat()
hawk.eat() #this cannot flee coz this is not from prey class
fish.eat() #this canbe flee or hunt coz this from both class 
fish.sleep()



