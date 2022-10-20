# def spam():
#     print("in spam")
#
#
# print(spam)
#
# display = spam
# print(display)
# print(spam)
#
# spam()
# display()  # called as monkey patching
#
#
# #####################
# def add(a, b):
#     print(a + b)
#     return add
#
#
# res = add(1, 2)  # called as monkey patching
# print(res)
# print(add)


#########################
# passing function as an argument
def demo():
    print("In demo")
    print(demo)


def sample(func):
    print(sample)
    print(func)


sample(demo)
