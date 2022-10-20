def last_ele(sequence):
    return sequence[-1]


print(last_ele("hello"))
print(last_ele([10, 20, 30]))
# print(last_ele())  # TypeError, missing posi args
print(last_ele)

##################################

# anonymous function using lambda expressions
# lambda args_name: statements --> only for single line statements
print(lambda sequence: sequence[-1])
res = lambda sequence: sequence[-1]
print(res)

print(res("hi"))
###################################

return_key = lambda dict_: dict_.keys()
print(return_key({"a": 1, "b": 2, "c": 3}))

return_key = lambda dict_: dict_.values()
print(return_key({"a": 1, "b": 2, "c": 3}))
