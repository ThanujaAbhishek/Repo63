char = "Are"
s = str(char)
if s[0] in "aeiouAEIOU":
    print(f"{char} starts with a vowel {s[0]}")
else:
    print(f"{char} does not starts with a vowel")