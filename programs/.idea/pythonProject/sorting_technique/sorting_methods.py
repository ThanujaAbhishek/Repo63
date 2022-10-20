# ls = [1, 45, 67, 21, 3, 5]
# ls.sort()
# print(ls)  # modifies original list
################################
# sorting list
# sorted() --> inbuilt func
# ls = [1, 45, 67, 21, 3, 5]
# print(sorted(ls))
# print(ls)

########################
# sorting string
# s = "hello"
# print(sorted(s))  # based on ASCII value, returns list
# print(s)
# print(sorted(s, reverse=True))
###########################
# sorting set
############################
# sorting dictionary
########################
# sorting tuple
###################


items = ["eat", "ate", "listen", "silent", "stressed", "tea", "desserts", "hai", "hello"]
d = {}
for item in items:
    sorted_value = "".join(sorted(item))
    if sorted_value not in d:
        d[sorted_value] = [item]
    else:
        d[sorted_value].append(item)

print(d)