#
d ={"a":1, "b":2, "c":3, "d":4}

for key in d:
    print(key)

for key in d.keys():
    print(key, end=" ")
print()
for items in d.items():
    print(items, end=" ")
print()
for values in d.values():
    print(values, end=" ")
print()
for key, value in d.items():
    print(key, value)

for key in enumerate(d):
    print(key)