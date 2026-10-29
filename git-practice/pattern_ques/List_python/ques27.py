#Check if List is Palindrome
List= [1, 2, 3, 2, 1]
def is_palindrome(list):
    #compare the list to its palindrome
    return list == list[::-1]

test1 = [1,2,3,2,1]
test2 = [1,2,3,2,1]
print(f"{test1} is palindrome? {is_palindrome(test1)}")
print(f"{test2} is palindrome? {is_palindrome(test2)}")