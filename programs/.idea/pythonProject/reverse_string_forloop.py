string = "Hello World"
res = ""
print(id(res))
for index in range(len(string)-1, -1, -1):
    res = res + string[index]
print(res)
print(id(res))

# range
"Hello World"
for index in range(len(string)):
    print((index, string[index]), end=" ")
print()

# enumerator()
for item in enumerate(string):
    print(item, end=" ")

print()

# printing only elements
for item in enumerate(string):
    print(item[1], end=" ")