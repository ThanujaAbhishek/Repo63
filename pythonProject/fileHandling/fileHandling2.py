import os
path = r"C:\Users\User\Desktop\files"
os.chdir(path)
# without context manager
# file_obj = open("sample.txt", "r")  # r --> read mode
# # print(file_obj.read())
# # print(file_obj.readline())  # if once read it won't read again
# # print(file_obj.readlines())  # in list in string format, reads from second line
# # print(file_obj.readline(15))
# print(file_obj.readlines(15))
# print(file_obj.closed)
# #file_obj.close()
# print(file_obj.closed)
# print(file_obj.readable())
# # print(file_obj.writable())  # file_obj = open("sample.txt", "w")

# file_obj = open("sample.txt", "w")  # r --> read mode
# file_obj.write("Hai")
# print(file_obj.write("Hello"))

# with context manager
# with open("sample.txt", "r") as file:
#     print(file.read())
#     print(file.readline())
#     print(file.readlines(10))
#     print(file.closed)
# print(file.closed)


with open("sample1.txt", "a") as file:
    # print(file.write("hello"))
    # print(file.write(" World\n"))
    # print(file.write("Good Morning\n"))
    file.writelines(["Python", " Programming\n", "Thank You\n"])  # just append but does not clear old contents


# create mode "x"
# with open("sample1.txt", "x") as file:
#     file.write("Hai")  # FileExistsError if we try to write into already existing file in create mode


# with open("sample1.txt", "r") as file:
#     print(file.read())
#     file.seek(0)
#     print(file.readline())


with open("sample1.txt", "r") as file:
    for line in file:  # iterating through file and reading line by line
        print(line)

#############################################################
