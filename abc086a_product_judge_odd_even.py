"""
偶数、奇数判定
"""
a = 3
b = 3

if a * b % 2 == 0:
    print("even")
else:
    print("odd")


"""
１７人を三人ずつのグループに分けて、余ったグループは１と考えると、グループは何グループできるか
"""
a = 16
b = 3

g = int((a + b - 1) / b)
print(f"{g} group")
