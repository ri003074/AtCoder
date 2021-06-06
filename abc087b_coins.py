A = 2  # 500yen
B = 2  # 100yen
C = 2  # 50yen
X = 200  # yen

print(10 % 3)  # 1
print(10 / 3)  # 3.333


coin_500 = 0
coin_100 = 0
coin_50 = 0

while X > 500:
    X -= 500
    coin_500 += 1
while X > 100:
    X -= 100
    coin_100 += 1
while X > 50:
    X -= 50
    coin_50 += 1


print(coin_500)
print(coin_100)
print(coin_50)

X = 200
res = 0
for a in range(A + 1):
    for b in range(B + 1):
        for c in range(C + 1):
            total = a * 500 + b * 100 + c * 50
            if total == X:
                print(total)
                res += 1

print(res)
