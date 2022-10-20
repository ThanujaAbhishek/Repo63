names = ["apple", "google", "apple", "yahoo", "google", "facebook", "gmail", "yahoo"]
d = {}
for item in names:
    if item not in d:
        d[item] = 1
    else:
        d[item] += 1
print(d)