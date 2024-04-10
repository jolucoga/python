# Lists are ordered collections of items that can be of different types.
# Lists are created by placing items inside square brackets [] and separating them with commas.
# Lists are mutable, which means that you can change the elements of a list after it has been created.
# You can access elements of a list using indexing.
# You can also use slicing to access a subset of elements from a list.
# You can use the + operator to concatenate two lists together.
# You can use the * operator to repeat a list multiple times.
# You can use the len() function to get the number of elements in a list.
# You can use the append() method to add an element to the end of a list.
# You can use the pop() method to remove an element from the end of a list.
# You can use the sort() method to sort the elements of a list in ascending order.
# You can use the reverse() method to reverse the elements of a list.
# You can use the index() method to get the index of a specific element in a list.
# You can use the insert() method to insert an element at a specific index in a list.
# You can use the remove() method to remove a specific element from a list.
# You can use the clear() method to remove all elements from a list.
# You can use the copy() method to create a copy of a list.
# You can use the count() method to get the number of occurrences of a specific element in a list.
# You can use the extend() method to add the elements of one list to another list.
my_list = [1, 2, 3]
my_list = ['STRING', 100, 23.2]
print(len(my_list))  # 3
my_list = ['one', 'two', 'three']
print(my_list[0])  # one
print(my_list[1:])  # ['two', 'three']
another_list = ['four', 'five']
print(my_list + another_list)  # ['one', 'two', 'three', 'four', 'five']
new_list = my_list + another_list
print(new_list)  # ['one', 'two', 'three', 'four', 'five']
new_list[0] = 'ONE ALL CAPS' # ['ONE ALL CAPS', 'two', 'three', 'four', 'five']
print(new_list) # ['ONE ALL CAPS', 'two', 'three', 'four', 'five']
new_list.append('six') # ['ONE ALL CAPS', 'two', 'three', 'four', 'five', 'six']
print(new_list) # ['ONE ALL CAPS', 'two', 'three', 'four', 'five', 'six']
new_list.append('seven') # ['ONE ALL CAPS', 'two', 'three', 'four', 'five', 'six', 'seven']
print(new_list) # ['ONE ALL CAPS', 'two', 'three', 'four', 'five', 'six', 'seven']
new_list.pop() # ['ONE ALL CAPS', 'two', 'three', 'four', 'five', 'six']
print(new_list) # ['ONE ALL CAPS', 'two', 'three', 'four', 'five', 'six']
popped_item = new_list.pop() # ['ONE ALL CAPS', 'two', 'three', 'four', 'five']
print(popped_item) # six
print(new_list) # ['ONE ALL CAPS', 'two', 'three', 'four', 'five']
new_list.pop(0) # ['two', 'three', 'four', 'five']
print(new_list) # ['two', 'three', 'four', 'five']

new_list = ['a', 'e', 'x', 'b', 'c']
num_list = [4, 1, 8, 3]
new_list.sort() # ['a', 'b', 'c', 'e', 'x']
print(new_list) # ['a', 'b', 'c', 'e', 'x'] 
num_list.sort() # [1, 3, 4, 8]
print(num_list) # [1, 3, 4, 8]

my_sorted_list = new_list.sort() # None
print(my_sorted_list) # None
type(my_sorted_list) # NoneType

num_list.reverse() # [8, 4, 3, 1]
print(num_list) # [8, 4, 3, 1]
