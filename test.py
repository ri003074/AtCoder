from collections import defaultdict

a = 3
b = 3

if a * b % 2 == 0:
    print("Even")
else:
    print("odd")

s = "101"

counter = 0
for i in s:
    if i == "1":
        counter += 1

print(f"counter={counter}")

N = 3
A = [16, 12, 24]

result = 0
while True:
    count = 0
    for i in range(len(A)):
        if A[i] % 2 != 0:
            break
        else:
            A[i] = A[i] / 2

    else:
        result += 1
        continue
    break

print(A)
print(result)


# 004 coins
A = 2
B = 2
C = 2
X = 100

count = 0
for a in range(A + 1):
    for b in range(B + 1):
        for c in range(C + 1):
            if a * 500 + b * 100 + c * 50 == 100:
                count += 1

print(f"coin kumiawase = {count}")

# 005 some sums
print("*** 005 ***")

print(834 % 10)

N = 20
A = 2
B = 5


def find_some_of_digits(val):
    sum = 0
    while val > 0:
        sum += val % 10
        val = val // 10

    return sum


print(find_some_of_digits(15))

res = 0
for i in range(1, N + 1):
    sum = find_some_of_digits(i)
    if sum >= A and sum <= B:
        res += i

print(res)

print("*** 006 ***")
N = 3
a = [2, 7, 4]
b = sorted(a)
b.reverse()

print(b)
alice = 0
bob = 0
for i in range(len(b)):
    if i % 2 == 0:
        alice += b[i]
    else:
        bob += b[i]

print(alice - bob)


print("*** 007 ***")

N = 4
Q = 3
d = [8, 10, 8, 6]

res = defaultdict(int)
for i in d:
    res[str(i)] += 1

print(len(res))


print("*** 008 ***")
N = 9
Y = 45000

for i in range(0, N + 1):
    for j in range(0, N + 1):
        for k in range(0, N + 1):
            if i * 10000 + j * 5000 + k * 1000 == Y and i + j + k == 9:
                print(i)
                print(j)
                print(k)
                break

print("*** 009 ***")

S = "dreameraser"
S = S[::-1]
print(S)
