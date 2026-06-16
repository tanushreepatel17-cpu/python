print("enter the marks of 5 subjects: ")
a,b,c,d,e = int(input()),int(input()),int(input()),int(input()),int(input())
if a>=33 and b>=33 and c>=33 and d>=33 and e>=33:# and operator is used to check all the conditions at once, if any one of the condition is false then it will return false and the result will be fail
    print("Result:  PASS")
    per = (a+b+c+d+e)/5
    print("Percentaage: ",per)
    if per>=60:
      print("FIRST DIVISION")
    
    elif per>=50: 
       print("SECOND DIVISION")
    
    else:
       print("THIRD DIVISION")

else:
    print("Result: FAIL")
        

