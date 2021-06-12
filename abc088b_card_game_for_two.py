N = 3
a = [2, 7, 4]

b = sorted(a, reverse=True)
print(b)

sum1 = 0
sum2 = 0
for index, val in enumerate(b):
    if index % 2 == 0:
        sum1 += val
    else:
        sum2 += val

print(sum1 - sum2)
