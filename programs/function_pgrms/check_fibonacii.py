num1 = 0
num2 = 1


def fibo_series(n):
    global num1
    global num2
    ls = []
    for _ in range(n):
        num3 = num1 + num2
        ls.append(num3)
        num1 = num2
        num2 = num3
    return ls


num = 89
list_1 = [num1, num2]
list_2 = fibo_series(num)
res = (*list_1, *list_2)
# print(res)
for ele in enumerate(res):
    if num in res:
        print(f"{num} is present in fibonacii series")
        break
else:
    print(f"{num} is not present in fibonacii series")


