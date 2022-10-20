num = 10
print(isinstance(num, int))  # True
print(isinstance(num, (complex, bool)))  # False
print(isinstance(num, (int, complex, bool)))  # True
