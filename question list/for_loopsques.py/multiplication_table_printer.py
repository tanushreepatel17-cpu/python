#rint the numtiplication table for a given number upto 10 but skip the fifth iteration

num = 3

for i in range(1 , 11):
    if i == 5:
        continue  #continue skips the rest of the current loop iteration and immediately starts the next iteration
                  #skip the next iteration

    print(f"{num} x {i} = {num * i}")