
a = "apple"
b = "hello"

for index in range(len(a)):
    print(a[index], b[index])

s1 = [1, 2, 3]
s2 = "hello"

# for index in range(len(s2)):
#     print(s1[index], s2[index]) --> IndexError, list out of ranfe
# hence use zip()