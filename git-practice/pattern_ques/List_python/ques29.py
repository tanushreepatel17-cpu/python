#List to Dictionary Conversion
#Keys= ["name", "age", "city"]
#Value= ["Alice", 25, "New York"]

def lst_to_dict(keys,value):
    return dict(zip(keys, value))
field = ["name", "age", "city"]
data = ["Alice", 25, "New York"]
result = lst_to_dict(field,data)

print(f"keys: {field}")
print(f"value: {data}")
print(f"resulting dict: {result}")