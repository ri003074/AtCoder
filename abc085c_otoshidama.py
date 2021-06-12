N = 9
Y = 45000

for i in range(N + 1):
    for j in range(N + 1):
        for k in range(N + 1):
            total = 10000 * i + 5000 * j + 1000 * k
            num = i + j + k

            if total == Y and num == 9:
                print("end")
                print(i)
                print(j)
                print(k)
                break


for i in range(N + 1):
    for j in range(N + 1):
        k = N - i - j
        total = 10000 * i + 5000 * j + 1000 * k
        num = i + j + k

        if total == Y and num == 9:
            print("end")
            print(i)
            print(j)
            print(k)
            break
