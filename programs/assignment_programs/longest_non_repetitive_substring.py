sentence = "This is a programming language and programming is fun"
words = sentence.split()
d = {}
for word in words:
    if words.count(word) == 1:
        if word not in d:
            d[word] = 1
        else:
            d[word] += 1

print(d)
longest_word = ""
for key, value in d.items():
    if len(longest_word) < len(key):
        longest_word = key
print(longest_word)

#######################################################################
# using comprehensions
lng_wrd = ""
list_ = [word for word in words if words.count(word) ==  1]
print(list_)
for word in list_:
    if len(lng_wrd) < len(word):
        lng_wrd = word
print(lng_wrd)
#########################################################################
# using max()
print(max([word for word in words if words.count(word) == 1], key = len))
