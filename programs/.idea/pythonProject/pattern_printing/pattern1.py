# *
# * *
# * * *
# * * * *
# * * * * *

# for row in range(6):
#     for col in range(row+1):
#         print("*", end=" ")
#     print()

# or
# for row in range(1, 6):
#     print("* "*row)

# or
# for row in range(1, 6):
#     print(f"{'* '*row:<10}")
######################################
# * * * * *
# * * * *
# * * *
# * *
# *
# for row in range(5, 0, -1):
#     print("* "*row)
###################################
#        *
#       * *
#     * * *
#   * * * *
# * * * * *
# for row in range(1, 6):
#     print(f"{'* '*row:>10}")
################################
# * * * * *
#   * * * *
#     * * *
#       * *
#         *
# for row in range(6, 0, -1):
#     print(f"{'* '*row:>10}")
#####################################
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
# for row in range(1, 6):
#     print(f"{'* '*row:^10}")
#####################################
# * * * * *
#  * * * *
#   * * *
#    * *
#     *
# for row in range(5, 0, -1):
#     print(f"{'* '*row:^10}")  # ^ --> char at
#######################################
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *
# for row in range(1, 6):
#     print(f"{'* '*row:^10}")
# for row in range(4, 0, -1):
#     print(f"{'* ' * row:^10}")
################################################
# *
# *
# *
# * *
# *
# * * *
# *
# * * * *
# for row in range(1, 5):
#     print("* ")
#     print("* "*row)