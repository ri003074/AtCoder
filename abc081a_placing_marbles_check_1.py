s = "101"
print(s.count("1"))

counter = 0
if s[0] == "1":
    counter += 1
if s[1] == "1":
    counter += 1
if s[2] == "1":
    counter += 1

print(counter)