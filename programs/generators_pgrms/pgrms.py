numbers = [1, 2, 3, 4]
sq_num = (num ** 2 for num in numbers)
print(list(sq_num))


# or

def squrae_(num_list):
    for num in num_list:
        yield num ** 2


print(list(squrae_(numbers)))
##########################
items = ["flipkart", 2021, "gmail", 1.2, [1, 2, 3], 2 + 3j, True]
tuple_values = (item for item in items if isinstance(item, (int, complex, float)))
print(tuple(tuple_values))
#############################
names = ["bob", "steve", "alex", "maya", "john"]


def odd_length(string_list):
    for name in string_list:
        if len(name) % 2 != 0:
            yield name


print(list(odd_length(names)))

# or

odd_len = (name for name in names if len(name) % 2 != 0)
print(list(odd_len))
#########################################################
items = ["flipkart", 2021, "gmail", 1.2, [1, 2, 3], 2 + 3j, True]
gen_seq = ((str(item))[::-1] for item in items if isinstance(item, (int, complex, float)))
print(list(gen_seq))


# or

def seq(items):
    for item in items:
        if isinstance(item, (int, float, complex)):
            yield (str(item))[::-1]


print("seq list: ", list(seq(items)))

###################################################################
import math


def inc_dec(pi_value, n):
    for i in range(n):
        yield round(pi_value, i)


print(list(inc_dec(math.pi, 4)))

# or

range_ = ((round(math.pi, i)) for i in range(6))
print(list(range_))
####################################################
n = 13
l = []


def fib(n):
    n1 = 0
    n2 = 1
    for _ in range(n):
        yield n1
        l.append(n1)
        n3 = n1 + n2
        n1, n2 = n2, n3
    for _ in l:
        if n in l:
            print(f"{n} is present in fibonacii series")
            break
        else:
            print(f"{n} is not present in fibonacii series")
            break


print(list(fib(n)))
list(fib(n))


######################################################################
# func takes variable no of positional arguments as i/p and check arg > 5
def func(*args):
    if len(args) > 5:
        print("No of positional argument > 5")
    else:
        print("No of positional argument <= 5")


func(3, 4, 5, 6, 8, 0)
func(1, 2)

##################################################################
string = "TRACXN"
n = 0
func = (string[n + 1::2] if n == 0 else string[n - 1::2])
print(func)
##################################################################
names = ["laura", "steve", "bill", "james", "greig", "scott", "alex", "ive", "edureka"]
vowel = (name for name in names if name[0] in "aeiouAEIOU")
print(list(vowel))


####################################################################
# sum the factorial of numbers from 1 to 5
def fact(j):
    prod = 1
    sum = 0
    # for i in range(n1, n2+1):
    #     for j in range(i):
    while j >= 1:
        prod = prod * j
        j -= 1
    print("fact:", prod)


"fact num: ", fact(1)

#############################################
l = [{"walmart": 7, "gmail": 5, "google": 6},
     {"walmart": 8, "gmail": 4, "google": 5},
     {"walmart": 9, "gmail": 3, "google": 4}]
d = sorted(l, key=lambda item: item["gmail"])
print(d)
#############################
d = {"walmart": 7, "gmail": 5, "facebook": 6}
print(sorted(d.items()))
print(sorted(d.items(), key=lambda item: item[0][-1]))
