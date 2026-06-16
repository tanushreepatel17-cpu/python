num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))
op = input("enter any operator: ")
if op == "+":
    print("your answer is :", num1+num2)
elif op == "-":
    print("your answer is :", num1-num2)
elif op == "*":
    print("your answer is :", num1*num2)
elif op == "/":
    print("your answer is :", num1/num2)
elif op == "%":
    print("your answer is :", num1%num2)
elif op == "**":
    print("your answer is :", num1**num2)
elif op == "//":
    print("your answer is :", num1//num2)
else:
    print("enter any operatror")