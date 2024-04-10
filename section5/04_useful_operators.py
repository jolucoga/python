# useful operators in python
# range, enumerate, zip, in, min, max, random, input
# range
mylist = [1, 2, 3]
for num in range(10): # 10 is the stop point
    print(num) # 0 1 2 3 4 5 6 7 8 9

for num in range(3, 10): # 3 is the start point
    print(num) # 3 4 5 6 7 8 9

for num in range(0, 10, 2): # 2 is the step size
    print(num) # 0 2 4 6 8

list(range(0, 11, 2)) # [0, 2, 4, 6, 8, 10]
print(list(range(0, 11, 2))) # [0, 2, 4, 6, 8, 10]

# enumerate
index_count = 0
word = 'abcde'
for letter in word:
    print(f'At index {index_count} the letter is {letter}')
    index_count += 1

index_count = 0
word = 'abcde'
for letter in word: # enumerate returns a tuple
    print(word[index_count]) # a b c d e
    index_count += 1

for item in enumerate(word):
    print(item) # (0, 'a') (1, 'b') (2, 'c') (3, 'd') (4, 'e')

for index, letter in enumerate(word):
    print(index) # 0 1 2 3 4
    print(letter) # a b c d e
    print('\n')

# zip
mylist1 = [1, 2, 3]
mylist2 = ['a', 'b', 'c']
for item in zip(mylist1, mylist2):
    print(item) # (1, 'a') (2, 'b') (3, 'c')

mylist1 = [1, 2, 3]
mylist2 = ['a', 'b', 'c']
mylist3 = [100, 200, 300]
for item in zip(mylist1, mylist2, mylist3):
    print(item) # (1, 'a', 100) (2, 'b', 200) (3, 'c', 300)

mylist1 = [1, 2, 3]
mylist2 = ['a', 'b', 'c']
mylist3 = [100, 200, 300]
for a, b, c in zip(mylist1, mylist2, mylist3):
    print(a) # 1 2 3
    print(b) # a b c
    print(c) # 100 200 300

# in
print('x' in [1, 2, 3]) # False
print('x' in ['x', 'y', 'z']) # True

d = {'mykey': 345}
print('mykey' in d) # True
print(345 in d.values()) # True

# min and max
mylist = [10, 20, 30, 40, 100]
print(min(mylist)) # 10
print(max(mylist)) # 100

# random
from random import shuffle
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shuffle(mylist)
print(mylist) # [5, 4, 2, 3, 6, 7, 1, 10, 9, 8]
shuffle(mylist)
print(mylist) # [5, 4, 2, 3, 6, 7, 1, 10, 9, 8]

from random import randint
print(randint(0, 100)) # 76
print(randint(0, 100)) # 24

# input
result = input('Enter a number here: ')
print(result) # 50
print(type(result)) # <class 'str'>

result = int(input('Enter a number here: '))
print(result) # 50
print(type(result)) # <class 'int'>


