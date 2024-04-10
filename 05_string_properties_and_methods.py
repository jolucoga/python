name = "Sam"
#name[0] = "P"  # TypeError: 'str' object does not support item assignment
# Strings are immutable in Python. This means that you cannot change the characters of a string once it has been created.
# If you try to change a character in a string, you will get a TypeError.
# This is different from other data types like lists, where you can change the elements of the list after it has been created.
# In Python, strings are immutable, which means that they cannot be changed after they are created.
# This is an important concept to understand when working with strings in Python.

last_letters = name[1:]
print(last_letters)  # am

# You can use string concatenation to create a new string that combines the original string with the new characters.
# This is a common pattern when working with strings in Python.
# You can use the + operator to concatenate two strings together.
name = "P" + last_letters
print(name)  # Pam

x = "Hello World"
print(x + " it is beautiful outside")  # Hello World it is beautiful outside
x = x + " it is beautiful outside"
print(x)  # Hello World it is beautiful outside

# You can use the * operator to repeat a string multiple times.
letter = "z"
print(letter * 10)  # zzzzzzzzzz

sum1 = 2 + 3
print(sum1)  # 5
sum2 = "2" + "3"
print(sum2)  # 23

# The split() method splits a string into a list of substrings based on a delimiter.
x = "Hello World"
print(x.upper()) # HELLO WORLD
print(x.lower()) # hello world
print(x.split()) # ['Hello', 'World']
print(x.split("l")) # ['He', '', 'o Wor', 'd']
print(x.split("o")) # ['Hell', ' W', 'rld']
print(x.split("e")) # ['H', 'llo World']

