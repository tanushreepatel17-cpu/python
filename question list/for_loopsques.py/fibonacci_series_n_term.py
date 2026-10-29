n = int(input("enter the number of terms: "))
a = 0
b = 1
print(a,b,end=" ")
for i in range(1, n):
    next_term = a + b
    print(next_term,end=" ")
    a = b
    b = next_term 