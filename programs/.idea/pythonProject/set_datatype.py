# set --> mutable datatype, and store object randomly inside heap area
# hence indexing and slicing not possible

s1 = set()  # empty set using set constructor
s2 = {}  # dictionary, not possible to create an empty set like this
s3 = {1, 2, 3}
s4 = {1, 2, 3, 1, 2}
print(s4)  # removes duplicates

# set allows only hasable values
# all immutable datatypes are hasable i.e, individual, strings, tuples are hasable

# if we include unhasable objects then it gives TypeError

# we cannot concatinate using + but we can concatinate using *
# print(s3+s4)
print((*s3, *s4))


# set methods
# union()
s11 = {1,2, 3, 4, 5}
s22 = {10, 20, 30, 4, 2}
print(s11.union(s22)) # creates a new set, does not modify s11 and s22

# intersection()
print(s11.intersection(s22))

# difference()
print(s11.difference(s22))  # s11 --> base set, s22 --> reference set, non-common ele of s11
print(s22.difference(s11))  # s22 --> base set, s11 --> reference set, non-common ele of s22

# symmetric_difference()
print(s11.symmetric_difference(s22))  # non-common ele of both sets
print(s22.symmetric_difference(s11))  # non-common ele of both sets

# update() --> returns nothing, modifies the base set
print(s11.update(s22))
print(s11)

# intersection_update()
s11 = {1, 2, 3, 4, 5}
s22 = {10, 20, 30, 4, 2}
s11.intersection(s22)
print(s11.intersection_update(s22))
print(s11)
print(s22)

# symmetric_difference_update()
s11 = {1, 2, 3, 4, 5}
s22 = {10, 20, 30, 4, 2}
print("symm_diff_update:", s11.symmetric_difference_update(s22))
s11.symmetric_difference_update(s22)
print("symm_diff_update s11:", s11)
print("symm_diff_update s22:", s22)

# add() --> both individual and collection datatype, similar to append
s11 = {1, 2, 3, 4, 5}
s22 = {10, 20, 30, 4, 2}
s11.add(10)
print("add to s11", s11)
s22.add("hai")
print("add to s22", s22)
# update() --> only collection datatype, similar to extend

# remove() --> throws KeyError if tried to remove a key not present

# discard() --> throws nothing if tried to remove a key not present

# pop() --> remove the element randomly and return the element
# print(set().pop()) -->empty set pop()--> KeyError
s11 = {1, 2, 3, 4, 5, 10}
print("pop():", s11.pop())
print("pop(): ", s11)  # set(), empty set

# clear()
s11 = {1, 2, 3, 4, 5, 10}
print("clear():", s11.clear())
print("clear():", s11)

# issuperset()

# issubset()

# isdisjoint()
