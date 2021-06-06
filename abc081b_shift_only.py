import time

N = 3
A = [16, 12, 24]

counter = 0
counter2 = 0

is_divide = True
start = time.time()
time.sleep(1)
while True:
    for i in range(len(A)):
        if A[i] % 2 == 0:
            A[i] = A[i] / 2
        else:
            is_divide = False

    if is_divide is False:
        break
    counter += 1
elapsed_time = time.time() - start
print(f"elapsed time:{elapsed_time}")

print(counter)

A = [16, 12, 24]
res = 10000
start = time.time()
time.sleep(1)
for a in A:
    tmp = a
    count = 0
    while tmp % 2 == 0:
        tmp = tmp / 2
        count += 1

    if res > count:
        res = count
elapsed_time = time.time() - start
print(f"elapsed time:{elapsed_time}")

print(res)
