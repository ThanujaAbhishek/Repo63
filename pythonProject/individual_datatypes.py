# all variables / identifiers are object of predefined class
# all the datatypes in python have predefined classes
# Ex: <class 'float'>,<class 'int'>, <class 'complex'>
# 2 ways to create object for int class
# directly by assigning the value a=10 or  by using className and passing value i.e. a = int(10)

##########################################
# int datatype
# default value of int = 0
a = 10
print("a: ", a)
print("type(a): ", type(a))
a1 = int()
print("default value of int no: ", a1)
##########################################
# float datatype
# default value of float no is 0.0
f = 10.2
print("f: ", f)
print("type() f", type(f))
f1 = float()
print("default value of float no: ", f1)
###########################################
# complex datatype
# default value of complex no is 0+0j/0j
c = 10+2j
print("c: ", c)
c1 = complex()
print("default value of complex no: ", c1)
# c2 = 12+j3
# print("c2: ", c2) --> NameError -->'12+j3' should be 12+3j
###########################################
# boolean datatype
# default value of boolean datatype is false
b = True
print("b: ", b)
b1 = bool()
print("default value of bool: ", b1)
