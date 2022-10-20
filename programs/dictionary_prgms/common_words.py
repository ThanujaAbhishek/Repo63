words = ["look", "into", "my", "eyes", "look", "into", "my", "eyes", "the", "eyes", "the", "eyes", "the",
         "eyes", "not", "around", "the", "eyes", "don't", "look", "around", "the", "eyes", "look", "into",
         "my", "eyes", "you're", "under"]
l = []
for word in words:
    if words.count(word) > 1:
        if word not in l:
            l.append(word)
print(l)