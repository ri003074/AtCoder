divide = ["dream", "dreamer", "erase", "eraser"]

S = "dreameraser"

for index, div in enumerate(divide):
    divide[index] = div[::-1]


# print(divide)

S = S[::-1]
# print(S[:2])
# print(S)

can = True
for i in range(len(S)):
    can2 = False
    for div in divide:
        print(S[: len(div)])
        print(div)
        if S[: len(div)] == div:
            can2 = True
            print("div")
            print(S)
            S = S[len(div) :]
            print(S)
            if S == "":
                break

    else:
        if not can2:
            can = False
            break
        else:
            continue

    break

if can:
    print("Yes")
else:
    print("No")
