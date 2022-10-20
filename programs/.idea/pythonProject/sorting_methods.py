# using sort()
ls = [10, 1, 3, 69, 74, 71]
print(ls.sort())
print(ls)
#########################
# Bubble sort technique
for _ in range(len(ls)):
    for i in range(len(ls) - 1):
        # temp = ls[i]
        if ls[i] < ls[i + 1]:
            ls[i], ls[i + 1] = ls[i + 1], ls[i]  # without using temp variable
            # ls[i + 1] = temp
print(ls)  # descending order by default
####################################################################################
for _ in range(len(ls)):
    for i in range(len(ls) - 1):
        # temp = ls[i]
        if ls[i] > ls[i + 1]:
            ls[i], ls[i + 1] = ls[i + 1], ls[i]  # without using temp variable
            # ls[i + 1] = temp
print(ls)  # ascending order
###################################################################################
sentence = "This is a programming session"
ls = sentence.split()
for _ in range(len(ls)):
    for i in range(len(ls) - 1):
        if len(ls[i]) < len(ls[i + 1]):
            ls[i], ls[i + 1] = ls[i + 1], ls[i]
print(ls)  # descending order length of words
###################################################################################