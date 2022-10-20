# to check whether number is prime using function

def prime_func(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return "Number is not a prime number"
        return "Number is prime"
    else:
        return "Number should be a positive number"


print(prime_func(5))
print(prime_func(6))
print(prime_func(1))


#####################################################

def prime_series(start: int, end: int):
    for num in range(start, end+1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                print(num, end=" ")


prime_series(1, 10)
