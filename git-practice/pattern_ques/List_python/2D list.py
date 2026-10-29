#2D list
fruit = ["apple", "orange", "banana", "coconut"]
vegetable = ["celery", "carrots", "p0tato"]
meats = ["chicken", "fish", "turkey"]

grocary = [fruit, vegetable, meats]

print(grocary)
# 2D list indexing
fruit =     ["apple", "orange", "banana", "coconut"]
vegetable = ["celery", "carrots", "p0tato"]
meats =     ["chicken", "fish", "turkey"]

grocary = [fruit, vegetable, meats]

print(grocary[0])
print(grocary[1])
print(grocary[2])
print(grocary[1][0])
print(grocary[2][0])
print(grocary[1][1])
print(grocary[1][2])
print(grocary[2][2])

#2D list nested loop
fruit =     ["apple", "orange", "banana", "coconut"]
vegetable = ["celery", "carrots", "p0tato"]
meats =     ["chicken", "fish", "turkey"]

grocary = [fruit, vegetable, meats]
for collection in grocary:
    for food in collection:
        print(food, end=" ")
    print()


#2d nested loop in tuple

fruit =     ("apple", "orange", "banana", "coconut")
vegetable = ("celery", "carrots", "p0tato")
meats =     ("chicken", "fish", "turkey")

grocary = (fruit, vegetable, meats)
for collection in grocary:
    for food in collection:
        print(food, end=" ")
    print()