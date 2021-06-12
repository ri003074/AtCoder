N = 20
A = 2
B = 5

total = 0
for i in range(N + 1):
    sum = 0
    for j in range(len(str(i))):
        sum += int(str(i)[j])

    if sum >= A and sum <= B:
        total += i

print(total)


def find_some_of_digits(num):
    sum = 0
    val = num
    while val > 0:
        sum += val % 10
        val = val // 10

    return sum


print(find_some_of_digits(834))
