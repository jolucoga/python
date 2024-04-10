# For loop example
# The for loop is used to iterate over a sequence (list, tuple, string) or other iterable objects. Iterating over a sequence is called traversal.
# Syntax:
# for element in sequence:
#     statement1
#     statement2
#     ...
# The sequence is an iterable object. The element is a variable that takes the value of the item inside the sequence on each iteration.
# Example:
# fruits = ['apple', 'banana', 'cherry']
# for fruit in fruits:
#     print(fruit)
# Output:
# apple
# banana
# cherry
# In this example, the for loop iterates over the list fruits. The variable fruit takes the value of each item in the list on each iteration.
# Note: The indentation is very important in Python. The statements inside the for loop must be indented with 4 spaces.
#

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in mylist: # num is just a variable name, you can use any name you want.
    print(num)

for jelly in mylist: # jelly is just a variable name, you can use any name you want.
    print(num)

for num in mylist:
    # Check for even
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd number: {num}')

list_sum = 0
for num in mylist:
    list_sum = list_sum + num # list_sum += num

print(list_sum) # 55

for letter in 'Hello World':
    print(letter)

tuple = (1, 2, 3)
for item in tuple:
    print(item)

mylist = [(1, 2), (3, 4), (5, 6), (7, 8)]
for item in mylist: 
    print(item)

for (a, b) in mylist:
    print(a)
    print(b)

d = {'k1': 1, 'k2': 2, 'k3': 3}
for item in d:
    print(item)

for item in d.items():
    print(item)

for key, value in d.items():
    print(key)
    print(value)

for value in d.values():
    print(value)
    