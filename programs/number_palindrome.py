num = 112
s = str(num)
if int(s[::-1]) == num:
    print(f"{num} is a palindrome number")
else:
    print(f"{num} is not a palindrome number")
