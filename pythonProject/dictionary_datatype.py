# empty dictionary
d = {}
d1 = dict() # using constructor

# with key-value pairs
d2 = dict({"a":1, "b":2, "c":3})
print(d2)

# using keywords
d3 = dict(x=20, y=30)
print(d3)

# using list of tuple
d4 = dict([("hai", 2), ("hello", 3)])
print(d4)

# using list
d5 = dict([["Good", 1], ["Morning", 2]])
print(d5)

d6 = {"a":1, "b":2, "c":3, "a":5}
print(d6) # latest value will be updated for repeated keys
# print(d6[0])  # KeyError, not possible to access through indexing

# keys will be single element
# d7 = {26, 1: "Republic day"} --> SyntaxError
d7 = {26:"Republic day"}

# keys can be iterables but the elements in the iterables should be hashable or immutable datatype
# hashable values as keys (Sets and Lists are not allowed as key)
# d8 = {[26, 1]:"Republic day"}
# print(d8)  # TypeError

# accessing the values through keys
d = {"Bengaluru":25, "Chennai":35, "Delhi":30}
print(d["Bengaluru"])
# print(d["chennai"])  # KeyError

# accessing the values through get()
# get(key, [value])
print(d.get("Bengaluru"))
print(d.get("chennai"))  # Returns none
print(d.get("delhi", "Key is not present"))  # key is mandatory

# adding key:value pair to dictionary
d["Noida"] = 32
print(d)
d.update({"Mysuru":27})
print(d)
d.update(Kolkata=35)
print(d)
d.setdefault("Kerala") # assigns value of Kerala=None
print(d)
print(d.setdefault("Manali", 20))
print(d)

d = {"Bengaluru":25, "Chennai":35, "Delhi":30}
print(d.setdefault("Chennai", 30))
print(d) # will not update Chennai value as 30
d["Chennai"] = 30
print(d)
d.update({"Chennai":35})
print(d)
d.update(Chennai = 45)
print(d)
from builtins import print

d = {"Bengaluru":25, "Chennai":35, "Delhi":30}
ls = ["a", "b", "c"]
print(ls)
# dict(l)  # ValueError, K-V pair sbp
print(d.fromkeys(ls))
print(dict.fromkeys(ls)) # fromkeys() allows to typecast any iterable to dictionary
print(dict.fromkeys(ls, 10))

# keys()
d = {"Bengaluru":25, "Chennai":35, "Delhi":30}
print(d.keys())

# values()
d = {"Bengaluru":25, "Chennai":35, "Delhi":30}
print(d.values())

# items()
d = {"Bengaluru":25, "Chennai":35, "Delhi":30}
print(d.items())

# removing element in dictionary
# pop(key)
d = {"Bengaluru":25, "Chennai":35, "Delhi":30}
# print(d.pop()) --> TypeError
print(d.pop("Delhi"))  # returns value of the key removed
# print(d.pop("Delhi"))  # KeyError
# popitem()
print(d.popitem())  # removes last item and returns it as tuple
# del keyword
d = {"Bengaluru":25, "Chennai":35, "Delhi":30}
del d["Chennai"]
print(d)

dd = {}
# print(dd.popitem())  # --> KeyError as dd is empty dictionary
# print(dd.pop())  # TypeError

# merging of two dictionaries
dd1 = {"a":1, "b":2}
dd2 = {"c":3, "d":4}
# print(dd1+dd2)  # TypeError
print({*dd1, *dd2})  # returns set of keys
print({**dd1, **dd2})
