# booleans in python
# True and False are the two boolean values in python
# They are used to represent truth values (other values can also be considered false or true)
# In numeric contexts (for example, when used as the argument to an arithmetic operator), they behave like the integers 1 and 0, respectively.
# The built-in function bool() can be used to cast any value to a boolean, if the value can be interpreted as a truth value
# The following values are considered false in python:
# False
# None
# 0 (int)
# 0.0 (float)
# '' (empty string)
# [] (empty list)
# {} (empty dictionary)
# () (empty tuple)
# set() (empty set)
# An empty set is considered True
# The following values are considered true in python:
# True
# Everything else
# Example:
# print(bool(True)) # True
# print(bool(False)) # False
# print(bool(0)) # False
# print(bool(1)) # True
# print(bool(0.0)) # False
# print(bool(0.1)) # True
# print(bool('')) # False
# print(bool('hello')) # True
# print(bool([])) # False
# print(bool([1])) # True
# print(bool({})) # False
# print(bool({'key': 'value'})) # True
# print(bool(())) # False
# print(bool((1,))) # True
# print(bool(set())) # False
# print(bool({1})) # True
# print(bool(None)) # False
# print(bool(set())) # False
# print(bool(set([1]))) # True
# print(bool(set([1, 1]))) # False
# print(bool(set([1, 2]))) # True
# print(bool(set([1, 2, 1]))) # False
# print(bool(set([1, 2, 3]))) # True
# print(bool(set([1, 2, 3, 1]))) # False
# print(bool(set([1, 2, 3, 4]))) # True

myvariable = True
print(myvariable) # True
print(type(myvariable)) # <class 'bool'>
myvariable = False
print(myvariable) # False
print(type(myvariable)) # <class 'bool'>
variableNone = None
print(variableNone) # None
print(type(variableNone)) # <class 'NoneType'>
