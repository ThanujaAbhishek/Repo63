# t = ("ciao", "adios", "hello", "world")
# vowel = lambda item: item[-1] in "aeiouAEIOU"
# print(list(filter(vowel, t)))
# print(list(map(vowel, t)))
# ########################################
# string1 = "ate"
# string2 = "eat"
# anagram = lambda string1, string2: "Is a anagram" if sorted(string1) == sorted(string2) else "Not a anagram"
# print((anagram(string1, string2)))
# # print(anagram())
# ##########################################
# num_list = [1, 2, 3, 4]
#
#
# def power(num, index):
#     res = num ** index
#     return res
#
#
# print(list(map(power, num_list, range(len(num_list)))))
# ################################################
# s = "abaaccrrbbddee"
# d = {}
# for char in s:
#     if char not in d:
#         d[char] = 1
#     else:
#         d[char] += 1
#
# print(d)
#
# # using lambda
#
# ###################################################
# numbers = [4, 8, 32, 76, 9]
#
#
# def multiple(num):
#     while True:
#         if num % 8 == 0:
#             print(num, end=" ")
#             break
#         num += 1
#
# list(map(multiple, numbers))
##################################################
# def prime(num):
#     if num > 1:
#         for i in range(2, num):
#             if num%i == 0:
#######################################################
l = [1, 2, 3, 4]


def func(num):
    if num % 2 == 0:
        return num ** 2


print(list(map(func, l)))

l = [1, 2, 3, 4]


def func(num):
    if num % 2 == 0:
        return num ** 2
    else:
        return num


print(list(map(func, l)))

l = [1, 2, 3, 4]


def func(num):
    if num % 2 == 0:
        return num ** 2
    else:
        return num


print("filter o/p:", list(filter(func, l)))

l = [1, 2, 3, 4]


def func(num):
    if num % 2 == 0:
        return num ** 2
    else:
        return False


print("filter o/p*:", list(filter(func, l)))

l = [1, 2, 3, 4]


def func(num):
    if num % 2 == 0:
        return num ** 2
    else:
        return 0


print("filter o/p:", list(filter(func, l)))

l = [1, 2, 3, 4]


def func(num):
    if num % 2 == 0:
        return num ** 2


print("filter o/p1:", list(filter(func, l)))

print("lambda map o/p:", list(map(lambda num: (num ** 2 if num % 2 == 0 else num), [1, 2, 3, 4])))
print("lambda filter o/p:", list(filter(lambda num: (num ** 2 if num % 2 == 0 else num), [1, 2, 3, 4])))
