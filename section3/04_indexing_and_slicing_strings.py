my_string = 'Hello World'
print(my_string)  # Hello World
# indexing
print(my_string[0])  # H
print(my_string[1])  # e
print(my_string[2])  # l
print(my_string[3])  # l

print(my_string[-1])  # d
print(my_string[-2])  # l
print(my_string[-3])  # r
# slicing
print(my_string[0:5])  # Hello
print(my_string[:5])  # Hello
print(my_string[6:])  # World
print(my_string[6:11])  # World

print(my_string[:])  # Hello World
print(my_string[::1])  # Hello World
print(my_string[::2])  # HloWrd
print(my_string[::3])  # HlWl
print(my_string[::4])  # Hoe
print(my_string[::5])  # H W
print(my_string[::6])  # Hr
print(my_string[::7])  # Hd
print(my_string[::8])  # H

print(my_string[::-1])  # dlroW olleH
print(my_string[::-2])  # drWolH
print(my_string[::-3])  # dWlH
print(my_string[::-4])  # doe
print(my_string[::-5])  # d H
print(my_string[::-6])  # dH
print(my_string[::-7])  # d

print(my_string[2:7:2])  # loW
print(my_string[2:7:3])  # lW
print(my_string[2:7:4])  # l

print(my_string[2:7:-1])  # empty string
print(my_string[7:2:-1])  # oW ol
print(my_string[7:2:-2])  # o l
print(my_string[7:2:-3])  # o

print(my_string[7:2:1])  # empty string
print(my_string[2:7:1])  # llo W
print(my_string[2:7:2])  # loW
print(my_string[2:7:3])  # lW
print(my_string[2:7:4])  # l

