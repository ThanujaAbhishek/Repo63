from itertools import zip_longest
s1 = [1, 2, 3]
s2 = "hello"
for item in zip(s1, s2):
    print(type(item))

# unpacking
for ele1, ele2 in zip(s1, s2):
    print(ele1)
    print(type(ele1))

# zip_longest(itrables, fillvalue = value)
for item in zip_longest(s1, s2):
    print(item)

for item in zip_longest(s1, s2, fillvalue = 0):
    print(item)

