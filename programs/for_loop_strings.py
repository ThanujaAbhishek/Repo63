from _operator import itemgetter

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

print()
# unpacking the item (tuple) inside for loop
for item in enumerate(string):
    print(item[0], item[1], end = ",")

print()
# unpacking the item and printing only index
for index, element in enumerate(string):
    print(index, end=" ")

print()
# unpacking the item and printing only elements
for index, element in enumerate(string):
    print(element, end=" ")