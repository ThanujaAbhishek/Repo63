# print(type(1_234_67))
# print(9.)
# print(bool(0)+bool(-1))  #
# print(bool(0+0j)+bool(1+1j))  #
# print((2+4i))  # --> SyntaxError, i/I cannot be used
# print(0123) # --> SyntaxError, 0 should not be a leading digit
# True = 30 # --> SyntaxError, cannot assign value to keyword

# ls = ["lilly@flower", "diary@chocolate", "lux@soap"]
# d = {}
# for items in ls:
#     item = items.split("@")
#     # print(item)
#     d[item[0]] = item[1]
# print(d)

# ls = ["google", "apple", "yahoo", "gmail"]
# res = [item for item in ls if len(item) < 6]
# print(res)

# names = ["apple", "google", "apple", "yahoo", "google", "facebook", "gmail", "yahoo", "gmail", "gmail"]
# d = {}
# for index, value in enumerate(names):
#     if value not in d:
#       d[value] = [index]
#     else:
#         # d[value].append(index)
#         d[value] += [index]
#
# print(d)

# ls = ["10.1", 12, True, "Hello", 13.2]
# d = {"a": "hello", "b": 100, "c": 10.1, "d": "world"}
# for key, value in d.items():
#     if isinstance(value, str):
#         d[key] = value[::-1]
#     else:
#         d[key] = value
# print(d)

# names = ["apple", "google", "apple", "yahoo", "yahoo", "google", "gmail", "yahoo"]
#
# # [("apple", 2), ("google", 2), ("yahoo", 3)]
# d = {}
#
# for name in names:
#     if names.count(name) >1:
#         if name not in d:
#             d[name] = 1
#         else:
#             d[name] += 1
#
# print(d)
# s = [(4, 56, 78), ("one", "two", "three")]
# d = {}
# keys, values = s
# print("keys:", keys)
# print("values:", values)
# if len(keys) == len(values):
#     for i in range(len(keys)):
#         if keys[i] not in d:
#             d[keys[i]] = values[i]
#     print(d)
# else:
#     print("length of keys and values are different")


