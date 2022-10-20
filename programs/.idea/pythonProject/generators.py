# generator is an iterator
def func():
    for i in range(3):
        return i

print(func())  # prints only 1 value and stops the execution
########################
def func():
    for i in range(3):
        yield i  # generator will generate sequence. yield keyword will pause the execution


print(func())
print(list(func()))

res = func()
print(next(res))  # next() is an inbuilt function which iterates and gives the result when asked. Lazy iteration
print(next(res))
print(next(res))
# print(next(res))  # StopIteration Error