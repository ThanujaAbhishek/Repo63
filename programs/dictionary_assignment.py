s = "abracadabraca"
d = {}
for char in s:
    d[char] = s.count(char)
print(d)

# without using inbuilt method
s = "abracadabraca"
d = {}
for char in s:
    if char not in d:
        d[char] = 1
    else:
        d[char] += 1
print(d)

# defaultdict()
from collections import defaultdict

s = "abracadabraca"
char_count = defaultdict(int)
for char in s:
    char_count[char] = char_count[char] + 1
print(char_count)

##################################################
# add to dict if its vowel
s = "hello world"
char_count = defaultdict(int)
for char in s:
    if char in "aeiouAEIOU":
        char_count[char] += 1
print(dict(char_count))
################################################
# add to dict if its vowel
s = "hello world"
d = {}
for char in s:
    if char in "aeiouAEIOU":
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1
print(d)
##################################################
# adding two list wrt indices
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
res = []
for ele1, ele2 in zip(a, b):
    res.append(ele1 + ele2)
print(res)
###################################################
# get the no of duplicates in a dict
names = ["apple", "google", "apple", "yahoo", "yahoo", "facebook", "apple", "gmail", "gmail", "gmail", "gmail"]
d = {}
for item in names:
    if item not in d:
        d[item] = 1
    else:
        d[item] += 1
print(d)
d1 = {}
for key, value in d.items():
    if value != 1:
        d1.setdefault(key, value)
print(d1)
#########################################################
names = ["apple", "google", "apple", "yahoo", "yahoo", "google", "gmail", "gmail", "gmail"]
d = {}
d1 = {}
d2 = {}
for index, item in enumerate(names):
    if item not in d:
        d1.setdefault(index, item)


print(d1)
