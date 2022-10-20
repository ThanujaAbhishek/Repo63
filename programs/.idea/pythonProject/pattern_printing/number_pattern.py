# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# pat = ""
# for row in range(1, 6):
#     pat = pat + " " + str(row)
#     print(pat)
#
# # or
# for row in range(1, 6):
#     for col in range(1, row + 1):
#         print(col, end=" ")
#     print()
##############################################################
# 5
# 5 4
# 5 4 3
# 5 4 3 2
# 5 4 3 2 1
# pat = ""
# for row in range(5, 0, -1):
#     pat = pat + " " + str(row)
#     print(pat)
########################################
 #         1
 #       1 2
 #     1 2 3
 #   1 2 3 4
 # 1 2 3 4 5
# pat = ""
# for row in range(1, 6):
#     pat = pat + " " + str(row)
#     print(f"{pat:>10}")
##########################################
# a
# a b
# a b c
# a b c d
# pat = ""
# start = "a"
# end = "d"
# for row in range(ord(start), ord(end)+1):
#     pat = pat+" "+chr(row)
#     print(pat)
# print()
############################################
#    a
#   a b
#  a b c
# a b c d
# pat = ""
# start = "a"
# end = "d"
# for row in range(ord(start), ord(end)+1):
#     pat = pat+" "+chr(row)
#     print(f"{pat:^10}")
#############################################

