# list comprehension is a unique way of quickly creating a list with Python.
# You can think of it as essentially a one line for loop built inside of brackets.
# 

# Example 1
mystring = 'hello'
mylist = []
for letter in mystring:
    mylist.append(letter)
print(mylist) # ['h', 'e', 'l', 'l', 'o']

# Example 2
mylist = [letter for letter in mystring]
print(mylist) # ['h', 'e', 'l', 'l', 'o']

# Example 3
mylist = [x for x in 'word']
print(mylist) # ['w', 'o', 'r', 'd']

# Example 4
mylist = [num for num in range(0, 11)]
print(mylist) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Example 5
mylist = [num ** 2 for num in range(0, 11)]
print(mylist) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Example 6
mylist = [x for x in range(0, 11) if x % 2 == 0]
print(mylist) # [0, 2, 4, 6, 8, 10]

# Example 7
celsius = [0, 10, 20, 34.5]
fahrenheit = [( (9/5) * temp + 32) for temp in celsius]
print(fahrenheit) # [32.0, 50.0, 68.0, 94.1]

# Example 8
results = [x if x % 2 == 0 else 'ODD' for x in range(0, 11)]
print(results) # [0, 'ODD', 2, 'ODD', 4, 'ODD', 6, 'ODD', 8, 'ODD', 10]

# Example 9
mylist = []
for x in [2, 4, 6]:
    for y in [100, 200, 300]:
        mylist.append(x * y) 
print(mylist) # [200, 400, 600, 400, 800, 1200, 600, 1200, 1800]

# Example 10
mylist = [x * y for x in [2, 4, 6] for y in [1, 10, 1000]]
print(mylist) # [2, 20, 2000, 4, 40, 4000, 6, 60, 6000]

