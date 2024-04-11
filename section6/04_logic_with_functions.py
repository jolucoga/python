# Functions for even numbers

def even_check(number):
  # result = number % 2 == 0
  # return result
  # a better way to do it is:
  return number % 2 == 0

print(f"Is 20 even? {even_check(20)}")
print(f"Is 21 even? {even_check(21)}")

def check_even_list(num_list):
  for number in num_list:
    if number % 2 == 0:
      return True
    else:
      # This is wrong because if the first number in the list is odd this will create a bug
      # it will return if the first number in the list is even or odd and will get out of function
      # without checking the rest of the list 
      #
      # return False
      pass

print(check_even_list([2,4,5]))
print(check_even_list([1,3,5]))

def check_even_list_2(num_list):
  even_numbers = [] # empty list to grab all even numbers in the list

  for number in num_list:
    if number % 2 == 0:
      even_numbers.append(number)
    else:
      pass
  return(even_numbers)

print(check_even_list_2([1,2,3,4,5]))
