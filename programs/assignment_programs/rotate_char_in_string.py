string = "Hello"  # o/p:- olHel
n = 3

ls = list(string)

for _ in range(n):
    value = ls.pop()
    ls.insert(0, value)
res = "".join(ls)
print(res)

# rotating words
sentence = "Hello World Good day"
ls = sentence.split()
for _ in range(n):
     word = ls.pop()
     ls.insert(0, word)
print(" ".join(ls))





