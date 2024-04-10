# Tuples are immutable
# Tuples are similar to lists, but they are immutable, which means that they cannot be changed after they are created.
# Tuples are created by placing items inside parentheses () and separating them with commas.
# Tuples are ordered collections of items that can be of different types.
# You can access elements of a tuple using indexing.
# You can also use slicing to access a subset of elements from a tuple.
# You can use the + operator to concatenate two tuples together.
# You can use the * operator to repeat a tuple multiple times.
# You can use the len() function to get the number of elements in a tuple.
# You can use the count() method to get the number of occurrences of a specific element in a tuple.
# You can use the index() method to get the index of a specific element in a tuple.
# You can use the in operator to check if an element is present in a tuple.
# You can use the not in operator to check if an element is not present in a tuple.
# You can use the for loop to iterate over the elements of a tuple.
# You can use the tuple() constructor to create a tuple from a list.

t = (1,2,3)
print(t)  # (1, 2, 3)
print(type(t))  # <class 'tuple'>
print(len(t))  # 3
print(t[0])  # 1

t = ('one', 2)
print(t)  # ('one', 2)
print(t[0])  # one
print(t[-1])  # 2

t = ('a', 'a', 'b')
print(t.count('a'))  # 2
print(t.index('a'))  # 0
print(t.index('b'))  # 2

my_list = ['a', 'b', 'c']
print(my_list)  # ['a', 'b', 'c']
my_list[0] = 'NEW'

# t[0] = 'NEW'  # TypeError: 'tuple' object does not support item assignment