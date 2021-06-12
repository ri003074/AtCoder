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
