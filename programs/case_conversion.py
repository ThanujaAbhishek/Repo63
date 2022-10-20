s = "K"
if ord("a") <= ord(s) <= ord("z"):
    s1 = chr(ord(s)-32)
    print(s1)
elif ord("A") <= ord(s) <= ord("Z"):
    s2 = chr(ord(s)+32)
    print(s2)
else:
    print(f"{s} is a special character")