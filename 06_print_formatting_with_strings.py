# Formatting with the .format() method
# A better way to format objects into your strings for print statements is with the string .format() method.
# The syntax is:
# 'String here {} then also {}'.format('something1', 'something2')
# For example:
# print('This is a string {}'.format('INSERTED'))  # This is a string INSERTED
#

print('This is a string {}'.format('INSERTED'))  # This is a string INSERTED  
print('The {} {} {}'.format('fox', 'brown', 'quick'))  # The fox brown quick
print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))  # The quick brown fox
print('The {0} {0} {0}'.format('fox', 'brown', 'quick'))  # The fox fox fox
print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))  # The quick brown fox
print('The {f} {f} {f}'.format(f='fox', b='brown', q='quick'))  # The fox fox fox

# Float formatting follows "{value:width.precision f}"
result = 100/777
print(result)  # 0.1287001287001287
print('The result was {r}'.format(r=result))  # The result was 0.1287001287001287

print('The result was {r}'.format(r=result)) # The result was 0.1287001287001287
print('The result was {r:1.3f}'.format(r=result))  # The result was 0.129

result = 104.12345
print('The result was {r:1.2f}'.format(r=result))  # The result was 104.12
print('The result was {r:1.5f}'.format(r=result))  # The result was 104.12345

# f-strings
# Introduced in Python 3.6, f-strings offer several benefits over the .format() method:
# 1. Readability: f-strings are more readable than the .format() method.
# 2. Speed: f-strings are faster than the .format() method.
# 3. Expressiveness: f-strings are more expressive than the .format() method.
# The syntax for f-strings is:
# f"String here {some_variable}"
# For example:
name = 'Jose'
print(f'Hello, his name is {name}')  # Hello, his name is Jose
name = 'Sam'
age = 3
print(f'{name} is {age} years old.')  # Sam is 3 years old.
