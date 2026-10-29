num = input("enter the no")
reverse = ""
for i in range (len(num) -1,-1,-1):
    reverse +=num[i]
if num == reverse:
    print("palindrome")
else:
    print("not palindrome")