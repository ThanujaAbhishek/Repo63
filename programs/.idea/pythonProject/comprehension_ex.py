s = "Good day good morning"
st = s.split()
d = {}
for word in st:
    d[word]  = len(word)
print(d)

# using comprehension
word_len = {word : len(word) for word in s.split()}
print(word_len)

#############################################################

d = {"a": 1, "b": 2, "c": 3}
d1 = {}
for key, value in d.items():
    temp = key
    key = value
    d1[key] = temp
print(d1)

# using comprehension

#############################################
s = "hello"
d = {}
for char in s:
    if s.count(char)>1:
        d[char] = s.count(char)
print(d)

char_count = {char:s.count(char) for char in s if s.count(char) > 1}
print(char_count)

################################################
s = "Hello Good Day Good Morning"
ls = s.split()
d = {}
for index, word in enumerate(ls):
    if index % 2 == 0:
        d[index] = word[::-1]
    else:
        d[index] = word
print(d)

# w = {index: word[::-1] if index % 2 == 0 else index: word for index, word in enumerate(s.split())}
# we cannot use/ initialize key more than once in comprehension
w = {index: word[::-1] if index % 2 == 0 else word for index, word in enumerate(s.split())}
print(w)
