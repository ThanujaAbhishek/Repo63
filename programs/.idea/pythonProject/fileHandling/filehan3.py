# # to print no of characters in sample.txt file
# import os
# path = r"D:\files"
# os.chdir(path)
# count = 0
# with open("sample.txt", "r") as file:
#     for line in file:
#         for char in line:
#             # print(char, end=" ")
#             count += 1
# print(count)
#
# # or using len()
#
# import os
# path = r"D:\files"
# os.chdir(path)
# count = 0
# with open("sample.txt", "r") as file:
#     for line in file:
#         count += len(line)
# print(count)
#
# ##########################################################
# # to count no of words in a file
# import os
# path = r"D:\files"
# os.chdir(path)
# count = 0
# with open("sample.txt", "r") as file:
#     for line in file:
#         words_list = line.split()
#         for word in words_list:
#             count += 1
#
# print(count)
#
# # or using len()
# import os
# path = r"D:\files"
# os.chdir(path)
# count = 0
# with open("sample.txt", "r") as file:
#     for line in file:
#         words_list = line.split()
#         count += len(words_list)
# print(count)
# #############################################
# # to print lines starting with vowels
# import os
# path = r"D:\files"
# os.chdir(path)
# with open("sample.txt", "r") as file:
#     for line in file:
#         if line.strip():
#             if line[0] in "aeiouAEIOU":
#                 print(line)
# ############################################
# # to print the line no and the no of words in a line in a file
# import os
# path = r"D:\files"
# os.chdir(path)
# with open("sample.txt", "r") as file:
#     for line_no, line in enumerate(file, start=1):
#         count = 0
#         if line.strip():  # removes the empty line
#             words_list = line.split()
#             for word in words_list:
#                 count += 1
#             print(line_no, count)
#
# # without using enumerate
# # import os
# # path = r"D:\files"
# # os.chdir(path)
# #
# # with open("sample.txt", "r") as file:
# #     line_no = 0
# #     for line in file:
# #         line_no += 1
# #         count = 0
# #         for word in line.split():
# #             count += 1
# #         print(line_no, count)
#
#
# ##########################
# # to read a file from last line
# import os
# path = r"D:\files"
# os.chdir(path)
# with open("sample.txt", "r") as file:
#     for line in (list(file))[::-1]:
#         print(line)
#
# # or
# with open("sample.txt", "r") as file:
#     for line in reversed(list(file)):
#         print(line)



################################
# to count the no of spaces in file
# import os
# path = r"D:\files"
# os.chdir(path)
# no_spaces = 0
# with open("sample.txt", "r") as file:
#     for line_no, line in enumerate(file, start=1):
#         ls = line.split()
#         if len(ls) > 1:
#             no_spaces += len(ls)-1
# print(no_spaces)
#
# # or
# with open("sample.txt", "r") as file:
#     count = 0
#     for line_no, line in enumerate(file, start=1):
#         count += line.count(" ")
# print(count)
#
# # or
# with open("sample.txt", "r") as file:
#     count = 0
#     for line in file:
#         for char in line:
#             if char == " ":
#                 count += 1
# print(count)

########################################################
# to create a dictionary with each word and its count pair in the file
# import os
# path = r"D:\files"
# os.chdir(path)
# d = {}
# with open("sample.txt", "r") as file:
#     for line in file:
#         ls = line.split()
#         for word in ls:
#             if word not in d:
#                 d[word] = 1
#             else:
#                 d[word] += 1
# print(d)
# #################################################
# # print most occuring word in file
# import os
# path = r"D:\files"
# os.chdir(path)
# d = {}
# with open("sample.txt", "r") as file:
#     for line in file:
#         ls = line.split()
#         for word in ls:
#             if word not in d:
#                 d[word] = 1
#             else:
#                 d[word] += 1
#
# print(sorted(d.items(), key=lambda item: item[1], reverse=True)[0])
########################################################################
# to print the nth line from a file
# import os
# path = r"D:\files"
# os.chdir(path)
# n = 5
# with open("sample.txt", "r") as file:
#     for line_no, line in enumerate(file, start=1):
#         if line_no == n:
#             print(line)
        # else:
        #     print(f"line no {n} does not exist in file")
        #     break
######################################
# to print 4th to 7th lines
# import os
# path = r"D:\files"
# os.chdir(path)
#
# with open("sample.txt", "r") as file:
#     for line_no, line in enumerate(file, start=1):
#         if line_no == 4 or line_no <= 7:
#             print(line)
##############################
# to print last n lines from a file
# import os
# path = r"D:\files"
# os.chdir(path)
# n = 2
# l = []
# with open("sample.txt", "r") as file:
#     for line_no, line in enumerate((list(file))[::-1], start=1):
#         while line_no <= n:
#             l.append(line)
#             break
#     for item in reversed(l):
#         print(item)
###########################################################
# ip address and their count
# import os
# path = r"D:\files"
# os.chdir(path)
# d = {}
# list_ = []
# with open("access-log.txt", "r") as file:
#     for line in file:
#         ls = line.split()
#         if ls != []:
#             list_.append(ls[0])
#     # print(list_)
#     for items in list_:
#         if items not in d:
#             d[items] = 1
#         else:
#             d[items] += 1
#
# print(d)

# or
# import os
# path = r"D:\files"
# os.chdir(path)
# d = {}
# with open("access-log.txt", "r") as file:
#     for line in file:
#         if line.strip():
#             words_list = line.split()
#         if words_list[0] not in d:
#             d[words_list[0]] = 1
#         else:
#             d[words_list[0]] += 1
#
# print(d)

# or using Counter class
# import os
# from collections import Counter
# path = r"D:\files"
# os.chdir(path)
# list_ = []
# with open("access-log.txt", "r") as file:
#     for line in file:
#         ls = line.split()
#         if ls != []:
#             list_.append(ls[0])
#     c = Counter(list_)
#     print(c)  # returns dictionary and sorts in descending order by default
#     print(c.most_common(2))
#     print(c.most_common(4))

#############################################
# # most occurring brand names from data.txt file
# import os
# path = r"D:\files"
# os.chdir(path)
# d = {}
# list_ = []
# with open("data.txt", "r") as file:
#     for line in file:
#         ls = line.split()
#         list_.append(ls[0])
#     print(list_)
#     for brands in list_:
#         if brands not in d:
#             d[brands] = 1
#         else:
#             d[brands] += 1
# print(sorted(d.items(), key=lambda item: item[1]))
# print(sorted(d, key=lambda item: item[1])[-1])

# or using default dict
import os
# from collections import defaultdict
# path = r"D:\files"
# os.chdir(path)
# dd = defaultdict(int)
# with open("data.txt", "r") as file:
#     for line in file:
#         brand_list= line.split()
#         dd[brand_list[0]] += 1
#         # dd[brand_list[0], brand_list[1]] += 1
# print(d)
################################################
# names of the countries from football.txt file
import os
from collections import Counter
path = r"D:\files"
os.chdir(path)
d = {}
country_list = []
with open("football.txt", encoding="UTF-8") as file:
    for line in file:
        list = line.split()
        country_list.append(list[1])
print(country_list)
# to get the count of countries
print(Counter(country_list))
#####################################
# import os
# from itertools import islice
# path = r"D:\files"
# os.chdir(path)
# with open("sample.txt") as file:
#     res = islice(file, 1, 5)  # in islice endIndex is mandatory
#     for i in res:
#         print(i)
###################################
# import os
# from collections import deque
# path = r"D:\files"
# os.chdir(path)
# with open("sample.txt") as file:
#     lines = deque(file, 5)  # deque(iterable, end), end-1 will be printed
#     for line in lines:
#         print(line)
######################################