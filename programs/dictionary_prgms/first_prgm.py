# sentence = "hello world welcome to python programming hi there"
# ls = sentence.split()
# for word in ls:
#     print(word[0], end="")

d = {"hello": 0, "world": 12, "welcome": 10, "to": 30, "python": 4}
print(d)
for key, value in d.items():
        # d[key] = key
        # temp = value
        # key = value
        # d[key] = temp
    if isinstance(value, int):
        d[value] = key
print(d)