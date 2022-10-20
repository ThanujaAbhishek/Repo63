b = 100


def add():
    b = 10
    return b


print(add())
###################################
a = 10


def add():
    global a
    return a


print(add())
#######################################

