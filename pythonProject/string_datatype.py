# Different ways to pass strings

s1 = "hello"
s2 = 'good morning'
s3 = """Great!"""
s5 = '''Good Day!'''
s6 = str("Good Luck!")
print("s6: ", s6)
s7 = '"Bye"'
print(s7)
s8 = "'Hi'"
print(s8)

# length of a string
print("Length of string s2: ", len(s2))

# empty string
string1 = str()
print("empty string: ", string1)
string2 = ""
print("empty string: ", string2)
string3 = ''
print("empty string: ", string3)

# default value of a string
default_string = str()
print("default_string: ", default_string)

# Regular strings
reg = "Pytho\n"
print("reg: ", reg)

# raw strings
# in real time if we want to use any path in the python code Ex: c:\users\..., then we need to use raw strings
# s = "\" or  s = r"\" not possible
rs1 = "\\"
rs2 = r"\\"
print("rs1", rs1)
print("rs2", rs2)
# rs3 = "C:\Users\User\AppData\Local\Programs\Python\Python310\Scripts"
# print(rs3)
# rs3 = "C:\\Users\\User\AppData\Local\Programs\Python\Python310\Scripts"
# print(rs3)
rs3 = r"C:\Users\User\AppData\Local\Programs\Python\Python310\Scripts"
print(rs3)

# string indexing
msg = "All the Best!"
print(msg[0:len(msg)]) # if len(msg)-1, then ! is not printed
print(msg[-1:-5]) # mandate to mention sv else empty string is printed
print(msg[-1:-6:-1])
print(msg[-6:-1])

# string slicing var_name[si:ei:sv]
# si --> 0, ei --> len(string), sv --> 1 are default values
a = "Good Morning"
print("forward dir:", a[0:len(a)]) # a[::] or a[:]
print("reverse string:", a[-1:-len(a)-1:-1]) # a[::-1]
print("alternate characters in forward dir:", a[::2])
print("alternate characters in reverse dir:", a[::-2])


# string formatting



