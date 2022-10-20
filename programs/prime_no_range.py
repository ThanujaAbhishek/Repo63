ls = []
for num in range(1, 21):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break

        else:
            print(num, end = " ")
            ls.append(num)
print()
print(ls)