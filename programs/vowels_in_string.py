s = "Hello World"
i = 0
while i < len(s):
    if s[i] in "aeiouAEIOU":
        print(s[i], end=" ")
    i += 1
