#Check if List is Sorted

def is_list_sorted(lst):
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            return False
    return True    
num1 = [10,20,30,40]
num2 = [10,20,30,25,40]

print(f"{num1} sorted? {is_list_sorted(num1)}")
print(f"{num2} sorted? {is_list_sorted(num2)}")

