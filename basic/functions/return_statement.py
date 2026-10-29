#return = statement used to end a function 
#  and send a result back to the caller

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last #here we concatinate first name and last name

full_name = create_name("spongebob", "squarpants")
print(full_name)