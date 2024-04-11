# methods are functions that are part of a class
# they are defined using the def keyword
# they always take the instance as the first argument
# by convention, we call the instance self
# methods can take additional arguments
# methods can return values
#

mylist = [1, 2, 3]
mylist.append(4)
print(mylist) # [1, 2, 3, 4]

mylist.pop()
print(mylist) # [1, 2, 3]

mylist.insert(2, 'inserted') # [1, 2, 'inserted', 3]
print(mylist) # [1, 2, 'inserted', 3]

mylist.remove('inserted') # [1, 2, 3]
print(mylist) # [1, 2, 3]



