s = "helloworld"
d = {}
for char in s:
    if s.count(char) > 1:
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1
print(d)