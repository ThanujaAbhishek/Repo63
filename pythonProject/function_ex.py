# msg1 = "Hello"  # global frame
# msg2 = "Hi"
#
# for i in range(5):
#     print(msg1)  # i is not used inside for loop
# # instead we can use throw away variable (_)
# for _ in range(5):
#     print(msg2)
#
#
# def func_name():  # once def keyword is located by interpreter it will
#     # create memory block in heap and copy the statements, only after locating func call it will
#     # enter to that memory loc and execute the statements
#     pass  # or ... to keep the function empty
#
#
# def func(message):  # in func defenition message: parameter/ formal argument
#     for _ in range(5):
#         print(message)
#
#
# func("Good Day!")  # function call --> actual arguments
#
#
# def add_func(a, b):
#     res = a + b  # No return statement i.e. return res
#     print(res)
#
#
# print(add_func(1, 2))  # prints None
#
#
# def sub_func(a, b):
#     res = a - b
#     return res
#
#
# print(sub_func(1, 2))
#
#
# # Types of arguments
#
# def add_func(a, b):
#     print(a + b)
#
#
# add_func(1, 2)  # positional arguments, based on position (Ex: isinstance())
#
# add_func(b=1, a=2)  # keyword argument (Ex: sort(key, reverse), print(end, sep))
#
# add_func(1, b=2)  # combination of positional and keyword arg,
# # positional arg followed by keyword arg
#
# # add_func(1, a=2) --> TypeError, multiple values for arg 'a'
#
# # add_func(1, a=2, b=2)  # --> TypeError, multiple values for arg 'a'
#
# # accept only positional arguments(/) --> before /
# def sub_func(a, b, /):
#     return a-b
#
#
# # sub_func(a=1, b=2)  # --> TypeError, a and b passed as keyword arg
# sub_func(1, 2)
#
#
# def addition(a, /, b):
#     return a+b
#
#
# addition(1, b=2)
# # addition(a=1, b=2)  # TypeError, a must be a positional arg
#
#
# # only keyword argument(*) --> after *
# def minus(*, a, b):  # a and b are keyword arg
#     return a-b
#
#
# def subtract(a, *, b):  # b is keyword arg and a is pos arg
#     return a-b
#
#
# # def sub(a, b, *): not possible as no arg after *
#
#
# # both pos and keyword arg
#
# def summation(a, /, *, b, c):
#     return a+b+c
#
#
# # '/' must be followed by '*'
# summation(1, b=2, c=3)
#
# # packing in func definition
#
# def adding():
#
#
#  # unpacking
#
# #############################################
#
#
#
# def len_func(iterable):
#     count = 0
#     for _ in iterable:
#         count += 1
#     return count
#
#
# print(len_func("Hello"))
# print(len_func([10, 20, 4 + 7j]))
# length = len_func({"a":1, "b":3, "c":4})


########################################################

#  # function annotations
# def add(a: int, b: int) -> int:
#     return a + b
#
#
# print(add(1, 10))
# print(add("hai", "hello"))
# print(add(True, 5+8j))

def last_index(num):

    string = str(num)
    return int(string[len(string)-1])


print(last_index(345))