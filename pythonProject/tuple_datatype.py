# empty tuple
t = ()
t1 = tuple()

#
t2 = (1, 2, 3, 4)
print("t2:", type(t2))
t3 = tuple((1, 2, 3, 4))
# single element tuple
t4 = ("hi",)
print(type(t4))
t5 = (1+3j)
print(type(t5))
t6 = ((1+3j),)
print(type(t6))

print(t2[2])
# t2[2] = 5
del t2
# del t2[2]

# count()

# index()

# concatinate tuple is possible
t8 = (1, 2, 3, 4)
t9 = ([10, 30], 40)
print(t8 + t9)
print((*t8, *t9))
print(t8, t9)