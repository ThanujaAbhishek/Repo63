# if conditiion:-
# Ex
num = 3
if num % 2 == 0:
    print("number is even")
    print("Hi")
else:
    print("number is odd")
    print("hello")

##########################
# for ref_var in iterable:
        # statements

s = "hello world"
for ref_var in s:
    print(ref_var)

########################
st = "hello world"
for item in range(len(st)):
    print(st[item], end=" ")

###########################
print()
s = "hello world"
for index in range(len(s)-1, -1, -1):
    print(s[index], end=" ")
#################
