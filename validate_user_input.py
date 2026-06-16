#vcalidate user input exercise
#username is not more than 12 characters
#usernaem must not contain spaces
#username must not contain digits

username = input("enter username: ")

if len(username) > 12: 
    print("username must not be more than 12 charactors")

elif not username.find(" ")== -1:# -1 if no space is found
    print("username must not contain spaces")

elif not username.isalpha():
    print("username must not contain digits")

else:
    print(f"welcome {username}")

