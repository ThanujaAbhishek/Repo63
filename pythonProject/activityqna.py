msg = "hai welcome to python"
print("reversed string:", msg[::-1])
print("join:", ",".join(msg.split()))

# String is immutable
# Ex
string1 = "Supriya"
print(string1.replace("Supriya", "A S"))
# performing replace operation using string1 but does not modify string1
print(string1)

# to find empty string
a = "";
print("length of a:", len(a))  # if len = 0, empty string

# list activity
names = ["apple", "google", "yahoo", "amazon", "facebook", "instagram", "microsoft"]
print(names[::-1])
print(names[2][3])
