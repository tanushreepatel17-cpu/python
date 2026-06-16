# logical operator = evaluate miltiple conditions (or,and, not)
#                or = at least one condition must be true
#                and = all conditions must be true
#                not = negates the condition(not false not true)
# or operator example
temp = 25
is_raining = False

if temp>35 or temp<0 or is_raining :
    print("the outdoor event is still cancelled")
else:
    print("the outdoor event is not cancelled")

#and operator example
temp = 24
is_sunny = True
 
if temp >=25 and is_sunny:
    print("it is hot outside")
    print("it is sunny")

elif temp <=25 and is_sunny:
    print("it is cold outside") 
    print("it is sunny")
elif 0 < temp <25 and is_sunny:
    print("it is warm outside")
    print("it is sunny")
elif temp>= 25 and not is_sunny:
    print("it is hot outside")
    print("it is sunny")
else:  
    print("it is cold outside") 
    print("it is not sunny")    