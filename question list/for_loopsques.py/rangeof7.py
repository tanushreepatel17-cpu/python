# #find the sum of all multiples of 7 between 1 and 500
# sum = 0
# for i in range(1,501):
#     if i % 7 == 0:
#         sum += i
#         print (sum)

s = 0
for num in range (7,501,7) :
    s+=num
    print(s)
