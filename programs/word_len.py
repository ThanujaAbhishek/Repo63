s1 = "python is a programming language"
s2 = s1.split()
print(s2)
d = {}
for word in s2:
    d[word] = len(word)
print(d)

####################
seq = [10, 20, 30]
seq1 = "hello"
seq2 = (10, "hai", 1+2j, True)
d1 = {}
d2 = {}
d3 = {}
for index, element in enumerate(seq):
    d1[index] = element
print(d1)
for index, element in enumerate(seq1):
    d2[index] = element
print(d2)
for index, element in enumerate(seq2):
    d3[index] = element
print(d3)

####################
s = "Good Morning and Good Day"
d = {}
s1 = s.split()
for word in s1:
    d[word] = s1.count(word)
print(d)

######################
s = "hai hello hai hello hello Good day day"
s1  = s.split()
d = {}
for word in set(s1):  # to reduce the no of duplicate iterations convert list s1 to set, so no duplicates in set
    d[word] = s1.count(word)
print(d)

# default dictionary