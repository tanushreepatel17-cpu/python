#nested loop = a loop within another loop )outer, inner)
#              outer loop:
#                  inner loop:
rows = int(input("enter the number of rows: "))
columns = int(input("enter the number of columns: "))
symbol = input("enter the number of symbol: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()