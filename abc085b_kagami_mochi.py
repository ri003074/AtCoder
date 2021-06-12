d = [8, 10, 8, 6]

dic = {}
for val in d:
    print(val)
    if str(val) not in dic:
        dic[str(val)] = 0
    dic[str(val)] += 1


print(dic)
