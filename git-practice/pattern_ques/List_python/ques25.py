#Find the Second Largest Number in a List
#define function
def get_second_largest(nums):

    #remove duplicate
    unique_nums = list(set(nums))

     #check condition
    if len(unique_nums) < 2:
        return None
    
    #sort the list in descending order
    unique_nums.sort(reverse = True)

    #return second element
    return unique_nums[1]

#test the function
number = [12,35,1,10,34,1,35]
result = get_second_largest(number)
print(f"second largest:{result}")
