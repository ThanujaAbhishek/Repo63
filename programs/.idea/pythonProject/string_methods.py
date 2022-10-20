# methods in str class (string)
# we can access methods using the instance /object of the respective class

# creating instance of str class
s = "Good Day!"
print(dir(s))

# 1.lower case
# string is immutable
# Ex:
s_lowercase = s.lower()
print("lower case:", s_lowercase)
# print(s) # even after converting to lower case the original object/string s does not get modified/changed

# 2. upper case
print("upper case:", s.upper())

# 3. swap case
print("swap case:", s.swapcase())

# 4. count(pass any character) --> int value
# gives the total no searched ch/substring in the given string, if not present it returns 0
print("count:", "hello".count("l"))
print("count:", "World".count("w"))
# checking for a substring using count()
print("count:", "super".count("per", 2))
# count(ch, si, ei) here count checks till (ei-1)
print("count:", "Hello World".count("l", 4, 9))

# 5. find() and rfind()
# find(substring, [si], [ei])
# rfind(substring, [si], [ei])
# to find the index value of a substring in a string
# returns the int value of the first occurrence of character/substring
print("index value using find():", "Today is a good day".find("day"))
print("index value using rfind():", "Today is a good day".rfind("day"))
# find() and rfind() will return -1 if ch/substring is not present in the given string
print("index value:", "Good".rfind("g"))


# 6. index(substring, si, ei)
# if ch/substring is not present then it will throw ValueError

# 7. replace(old_substring/ch, new_substring/ch, [count])
# how many ch has to be replaced is given by count


# 8. startswith(substring, [si], [ei]) --> boolean
# s = "hello world"
# print(s.startswith("ello"))
# print(s.startswith("ello", 1))
# print(s.startswith("ld", 9, 10))
# print(s.startswith("ld", 9, 11))

# 8.a. endswith(substring, [si], [ei]) --> boolean

# 9. split(ch/substring, no_of_splits) --> List
# 9.a. rsplit(ch/substring, no_of_splits) --> List
# if ch not present in given string then it prints original string inside a list

# 10. join() --> String

# 11. strip()
# sww = "$*5$ghsg$*&$"
# print(sww.strip("$"))
# see = "901129198"
# print(see.strip("1"))
# srr = "119011291981"
# print(srr.strip("1"))
# stt = " Hi Hello "
# print(stt.strip())

# 11.a. lstrip()

# 11.b. rstrip()

# 12. isalnum()
# print("Hello world".isalnum())
# print("Hello".isalnum())
# print("123".isalnum())
# print("Hello123".isalnum())

# 13. isalpha()

# 14. isdidgit()

# 15. islower()

# 16. isupper()

# 17. isspace()
