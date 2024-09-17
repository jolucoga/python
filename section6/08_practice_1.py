def lesser_of_two_evens(a,b):
  if a%2 == 0 and b%2 == 0:
    if a < b:
      result = a
    else:
      result = b
  else:
    if a > b:
      result = a
    else:
      result = b
    return result
  
def lesser_of_two_evens_2(a,b):
  if a%2 == 0 and b%2 == 0:
    return min(a,b)
  else:
    return max(a,b)
  
print(lesser_of_two_evens_2(21,10))