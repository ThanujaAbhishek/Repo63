from copy import deepcopy

# # creating a list
# from calendar import prcal
# from itertools import product
# # creating list constructor
#
# # empty list
#
#
# # indexing list
# nums = [1, 2, 3, 49]
# # 1st ele
# print(nums[0])
# # last ele
# print(nums[-1])
#
# # indexing
# elements = [1, "hello", 1.23, True, 4+6j]
# print(elements[0])
# print(elements[1])
# print(elements[1][1])
# print(elements[1][-1])
# print(elements[-1])
#
# # slicing
# # 1st n values
# print(elements[:3])
# # last n values
# print(elements[-2:])
#
# ele1 = [1,2,3]
# ele2 = [4,5,6]
# print(ele1, ele2)  # packing
# print(ele1+ele2)
# ele3 = print(*ele1, *ele2)  # unpacking
# print(type(ele3))
#
# # list methods
# names = ["apple", "google", "yahoo", "amazon", "facebook", "instagram", "microsoft"]
#
# # append()
# names.append(10)  # returns nothing, we need to print the appended original list
# print(names)
#
# # extend()
# names.extend("hai")
# print(names)
# names.extend([1, 2, 4])
# print(names)
# # names.extend(10)
# # print(names) -->TypeError, only collection datatypes can be extended
#
# # insert()
# print([1,2].insert(0, "hello"))
#
# # remove() --> returns nothing, can give index/ element itself,
# # if element not present, throws ValueError
#
# # pop() --> returns the removed element, need to pass the index,
# # if index not present then throws IndexError
#
# # clear() --> returns nothing, inside heap it will be having []
# # i.e. list will not be deallocated but will be an empty list
#
#
# # del keyword
#
# # creating a copy of the list


a = [1, 2, 3, [2, 4, 5]]
# b = a[:]
# print(id(a))
# print(id(b))
#
# # copy()
#
# # Nested list
# an = []
#
# # shallow copy
print(a.copy())
b = a.copy()
print(b)
print(id(a[-1]))
print(id(b[-1]))

# # deep copy
print(deepcopy(b))
c = deepcopy(a)
print(c)
print(id(b[-1]))
print(id(c[-1]))

# # sort(key, reverse) --> returns nothing
# # by default reverse = False, so sorts in ascending order and key = none
# # if key is none, then sorts according to ASCII value
# names = ["apple", "google", "yahoo", "amazon", "facebook", "instagram", "microsoft"]
# # based on reverse = true
# names.sort(reverse = True)
# print(names)
# # based on key = len
# names = ["apple", "google", "yahoo", "amazon", "facebook", "instagram", "microsoft"]
# names.sort(key = len)
# print(names) # if 2 strings are having same len, then sorts based on the position of the string
# names1 = [1, "hello", 1.23]  # heterogeneous list
# # names1.sort()
# # print(names1)  # TypeError, cannot sort heterogeneous list
# # based on both key, reverse --> it will sort first on len and then reverse it
# names = ["apple", "google", "yahoo", "amazon", "facebook", "instagram", "microsoft"]
# names.sort(key = len, reverse = True)
# print(names)
#
# # index(), no si and ei
# # ValueError if value not present in list
#
# # count(), no si and ei
# # if value not present returns 0
#
# # string into a list
# # split
# # list constructor
#
# # list into string
# # using join
# s = "Hi"
#
# ls = [True, False]
# ls.sort()
# print(ls)
# ls = [True, False, None]
# # ls.sort() # TypeError
# print(ls)
#
# l1 = [1, 2, 3]
# print(l1.insert(9, "hi"))
# print(l1)
