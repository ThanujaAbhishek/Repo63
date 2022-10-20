# using lambda function
numbers = [1, 2, 3, 4, 5]
squares_ = lambda iterable: [num ** 2 for num in numbers]
print(squares_(numbers))
###########################
# using for loop
ls = []
squares_of = lambda num: num ** 2
for num in numbers:
    res = squares_of(num)
    ls.append(res)
print(ls)
#################################
# using map()
numbers = [1, 2, 3, 4, 5]
op = map(squares_of, numbers)
print(op)
print(list(op))
