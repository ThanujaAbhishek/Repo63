a = 10
b = 20


def spam(n1, n2):
    return n1 + n2


if __name__ == "__main__":
    print(spam(1, 2))


print(__name__)  # when file1s exe --> __main__
# when file 2 is exe -> file1
