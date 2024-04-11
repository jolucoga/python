def say_hello(): # no parameter
    print('hello')
    print('how')
    print('are')
    print('you')
    
say_hello() # hello

def say_hello(name): # name is a parameter
    print(f'Hello {name}!')

say_hello('Jose') # Hello Jose!

def say_hello(name='Default'): # Default is the default value
    print(f'Hello {name}!')

say_hello() # Hello Default!

def add_num(num1, num2):
    return num1 + num2 # return is used to return a value from the function

result = add_num(10, 20) # 10 and 20 are arguments
print(result) # 30

def print_result(a, b): 
    print(a + b)
    
def return_result(a, b): 
    return a + b

result = print_result(10, 20) # 30
print(result) # None

result = return_result(10, 20) # 30
print(result) # 30

def myfunc(a, b):
    print(a + b)
    return a + b

result = myfunc(10, 20) # 30
print(result) # 30

def sum_numbers(num1, num2): 
    return num1 + num2

result = sum_numbers(10, 20) # 30
print(result) # 30

# You need to be careful with the data types
# result = sum_numbers(10, '20') # TypeError: unsupported operand type(s) for +: 'int' and 'str'
result = sum_numbers('10', '20') # 1020
print(result) # 1020

# you can use print and return in the same function
def myfunc(a, b):
    print(a + b)
    return a + b
    
result = myfunc(10, 20) # 30
print(result) # 30

