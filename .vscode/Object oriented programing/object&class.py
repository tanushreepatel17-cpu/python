#object = A "bundle" of related attributes (variables) and methods functions
#          Ex. phone, cup, book
#you need a "class" to create any objects

#class = (blueprint) used to design the structure and layout of an object


#objects
#from car import Car
#car1 = Car("Mustang", 2024, "red", False)
#car2 = Car("corvette", 2025, "blue", True)
#car3 = Car("charger", 2026, "yellow", True)


#attributes:
class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model  #assign the attributes here
        self.year = year
        self.color = color
        self.for_sale = for_sale

#CONSTRUCT CAR object
car1= Car("Safari", 2026, "black", False)
car2 = Car("thar", 2026, "red", True)
car3 = Car("BMW", 2025, "white", True)
print(car3.model)
print(car3.year)
print(car3.color)
print(car3.for_sale)


