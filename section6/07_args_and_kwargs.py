# Example

def my_func(a,b):
  # Returns 5% of the sum of a and b
  return sum((a,b)) * 0.05

print(my_func(40,60))

def myfunc(*args):
  return sum(args) * 0.05

# args takes a undefine number of arguments for the function and treat them as a tuple
def myfunc2(*args):
  for item in args:
    print(item)

myvar = myfunc(10,20,30,40,50) 
print(myvar)

myfunc2(10,20,30,40)

# kwargs takes a undefine number of arguments for the funtion and treat them as a dictionary.
def myfunc3(**kwargs):
  if 'fruit' in kwargs:
    print('My fruit of choice is {}'.format(kwargs['fruit']))
  else:
    print('I did not find any fruit here')

myfunc3(fruit = 'apple')
# Since it is a dictionary this is a valid function call by adding veggie to it.
myfunc3(fruit = 'apple', veggie = 'lettuce')

def myfunc4(*args,**kwargs):
  print(args)
  print(kwargs)
  print('I would like {} {}'.format(args[0],kwargs['food']))

myfunc4(10,20,30,fruit='orange',food='eggs',animal='dog')