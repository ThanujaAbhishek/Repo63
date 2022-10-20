num1 = 0
num2 = 1


def fibo_series(n):
    global num1
    global num2
    for _ in range(n):
        print(num1, end=" ")
        num3 = num1 + num2
        num1 = num2
        num2 = num3
    print()
    print(num1)


fibo_series(15)
