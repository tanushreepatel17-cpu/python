a=int(input("Enter a number: "))
temp=a
rev=0
while temp>0:
    dig=temp%10
    rev=rev*10+dig
    temp=temp//10
if a==rev:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")