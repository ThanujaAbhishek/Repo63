# def positive_op(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         return abs(res)
#
#     return wrapper
#
#
# @positive_op  # subtraction = positive_op(subtraction)
# def subtraction(a, b):
#     return a - b
#
#
# print(subtraction)
# print(subtraction(1, 2))
#
#
# ##################################################################
#
# def outer(func):
#     def wrapper(*args, **kwargs):
#         for _ in range(3):
#             func(*args, **kwargs)
#
#     return wrapper
#
#
# @outer
# def add(a, b):
#     print(a + b)
#
#
# add(1, 2)
#
# ####################################################################
# count = 0
# d = {}
#
#
# def outer(func):
#     def wrapper(*args, **kwargs):
#         global count
#         res = func(*args, **kwargs)
#         count += 1
#         if func.__name__ not in d:
#             d[func.__name__] = 1
#         else:
#             d[func.__name__] += 1
#         return res
#
#     return wrapper
#
#
# @outer
# def multiplication(a, b):
#     return a * b
#
#
# @outer
# def division(a, b):
#     return a / b
#
#
# print(multiplication(2, 4))
# print(division(8, 4))
# print(multiplication(12, 2))
# print(division(12, 4))
# print(multiplication(4, 8))
# print("Total no of function calls:", count)
# print(d)

##############################################################
# count = 0
#
#
# def dec_funcs(func):
#     global count
#     count += 1
#
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         print(res)
#
#     return wrapper
#
#
# @dec_funcs  # display = dec_funcs(display)  --> display = wrapper as dec_funcs returns wrapper in line 84
# def display(msg):
#     return msg
#
#
# @dec_funcs  # copy = dec_funcs(copy)
# def copy(msg):
#     return msg
#
#
# @dec_funcs  # spam = dec_funcs(spam)
# def spam(msg):
#     return msg
#
#
# spam("Hello")
# print("The number of decorated functions is:", count)
################################################################
# import time
#
#
# def delays(func):
#     def wrapper(*args, **kwargs):
#         if func.__name__ == copy:
#             time.sleep(4)
#         elif func.__name__ == spam:
#             time.sleep(6)
#         else:
#             time.sleep(8)
#         res = func(*args, **kwargs)
#         return res
#
#     return wrapper
#
#
# @delays  # copy = dec_funcs(copy)
# def copy(msg):
#     return msg
#
#
# @delays  # spam = dec_funcs(spam)
# def spam(msg):
#     return msg
#
#
# @delays
# def display(msg):
#     return msg
#
#
# print(copy("Hi"))
# print(spam("Hello"))
# print(display("Good"))


#########################################
# import time
#
#
# def parameter(n):
#     def outer(func):
#         def wrapper(*args, **kwargs):
#             time.sleep(n)
#             res = func(*args, **kwargs)
#             print(res)
#
#         return wrapper
#
#     return outer
#
#
# @parameter(5)
# def add(a, b):
#     return a + b
#
#
# add(1, 2)


##################################################################
def param(n):
    def display_stat(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                res = func(*args, **kwargs)
                print(res)
        return wrapper
    return display_stat


@param(4)
def add(a, b):
    return a + b


@param(5)
def sub(a, b):
    return a - b


add(1, 2)
sub(4, 2)
##################################################
# nested decorators

def log():
    def wrapper():
        pass

def register():
    def inner():
        pass

@log
@register
def main():
    pass
