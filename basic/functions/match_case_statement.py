#Match-case statement(Switch): An alternative to using many "elif" statements
#                              Exercise some code if a value matches a 'case'
#                              Benefits: cleaner and syntax is more readable



def day_of_week(day):
    match day:
        case 1:
            return "it is sunday"
        case 2:
            return "it is monday"
        case 3:
            return "it is tuesday"
        case 4:
            return "it is wednesday"
        case 5:
            return "it is thursday"
        case 6:
            return "it is friday"
        case _:
            return "it is saturday"
print(day_of_week(5))


#exercise
def is_weekend(day):
    match day:
        case "saturday" | "sunday":
            return True
        case "Monday" | "tuesday" | "wednesday" | "thursday" | "friday":
            return False
        case _:
            return False
print(is_weekend("Friday"))