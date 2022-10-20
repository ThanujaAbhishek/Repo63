s1 = {10, 20, 30}

for element in s1:
    print(element, end=" ")

print()
# using range() we cannot iterate through set as it cannot be indexed or sliced

# enumerate() --> returns as tuple
for item in enumerate(s1):
    print(item, end=" ")
   # print(item[0], end=" ")
   # print(item[1], end=" ")
print()
# unpacking the items and printing the index and elements
for index, element in enumerate(s1):
    print(index, element, end=",")

print()
#unpacking items and printinf only index
for index, element in enumerate(s1):
    print(index, end=" ")

print()
#unpacking items and printinf only elements
for index, element in enumerate(s1):
    print(element, end=" ")
