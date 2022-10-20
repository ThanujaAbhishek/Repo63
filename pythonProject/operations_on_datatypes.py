import math

# operations on integer
num1 = 10
num2 = 20

print("The addition result is: ", num1+num2)
print(num1 - num2)
print(abs(num1 - num2))
print(num1 * num2)
print(num1 / num2)
print(num1 % num2)


# floor operator '//' --> returns only whole number in quotient
print("Division operator: ", 20 / 3)  # 6.6666
print("Floor operator: ", 20 // 3)  # 6

# Exponent operator '**'
print(2 ** 2)

# abs() inbuilt function --> removes -ve sign
print(abs(-92))

# divmod() inbuilt function --> tuple of quotient and remainder
print("divmod(4, 3): ", divmod(4, 3))  # (1, 1) --> returns(x // y, x % y)
print("divmod(10, 20): ", divmod(10, 20))  # (0, 10)

######################################################

# functions on float

a = -1.3
print(abs(a))  # 1.3
print(round(3.141))   # 3
print(round(3.141, 1))  # 3.1
print(round(3.161, 1))  # 3.2
print(round(2.5))   # 2
print(round(1.5))   # 2

# trunc() is an inbuilt function inside the inbuilt module math
a = 23.948
print(math.trunc(a))  # 23
# print(math.trunc(a, 2)) --> TypeError
print(math.trunc(3.78))  # 3

# complex
# num = 10+j8
# print(num)  # --> NameError bcause j8
