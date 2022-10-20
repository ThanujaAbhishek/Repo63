import math

# int num
num = 10
print(float(num))  # 10.0
print(complex(num))  # (10+0j)
print(bool(num))  # True, num != 0

# float num
num1 = 1.3
print(int(num1))  # 1
print(complex(num1))  # (1.3+0j)
print(bool(num1))  # True

# complex num
num2 = 1+2j
# print(int(num2))  # TypeError
# print(float(num2))  # TypeError
print(bool(num2))  # True


# boolean value
num3 = True
num4 = False

print(int(num3))  # 1
print(float(num3))  # 1.0
print(complex(num3))  # (1+0j)

print(int(num4))  # 0
print(float(num4))  # 0.0
print(complex(num4))  # (0j)

#############################################################
# round(), divmod(x,y) inbuilt function
print(round(1.5))  # 2
print(round(2.5))  # 2
print(round(1.2346, 3))  # 1.235
a = 23.948
print(round(a))  # 24
print(round(a, 2))  # 23.95

#############################################################

