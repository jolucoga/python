# operators in python
# +, -, *, /, %, **, //, =, +=, -=, *=, /=, %=, **=, //=, ==, !=, >, <, >=, <=, and, or, not, &, |, ^, ~, <<, >>, in, not in, is, is not

# Arithmetic Operators
# +, -, *, /, %, **, //
# + addition
# - subtraction
# * multiplication
# / division
# % modulus
# ** exponentiation
# // floor division

# Comparison Operators
# ==, !=, >, <, >=, <=
# == equal
# != not equal
# > greater than
# < less than

# Logical Operators
# and, or, not
# and logical and
# or logical or
# not logical not

print(2 == 2) # True
print(2 != 2) # False
print('hello' == 'hello') # True
print('hello' == 'Hello') # False
print(2.0 == 2) # True


# Membership Operators
# in, not in
# in present in
# not in not present in
print('h' in 'hello') # True
print('h' not in 'hello') # False
print('z' in 'hello') # False
print('z' not in 'hello') # True

# Identity Operators
# is, is not
# is same object
# is not not same object
a = 10
b = 10
print(a is b) # True
print(a is not b) # False
a = 10
b = 20
print(a is b) # False
print(a is not b) # True


print(1 < 2 and 2 < 3) # True
print(1 < 2 and 2 > 3) # False
print(1 < 2 or 2 > 3) # True
print(1 > 2 or 2 > 3) # False
print(not 1 < 2) # False
print(not 1 > 2) # True
print('h' == 'h' and 2 == 2) # True


