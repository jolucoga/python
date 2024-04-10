# Description: This file demonstrates how to read and write files in Python
# Run: python3 12_IO_In_Out.py
myfile = open('section3/mytextfile.txt')
print(myfile.read()) # This will print the contents of the file
print(myfile.read()) # This will print an empty string because the file has already been read

myfile.seek(0) # This will move the cursor to the beginning of the file
content = myfile.read()
print(content) # This will print the contents of the file
myfile.seek(0) # This will move the cursor to the beginning of the file
print(myfile.readlines()) # This will print the contents of the file as a list of lines
myfile.close() # The file is closed after reading

with open('section3/mytextfile.txt') as my_new_file:
    content = my_new_file.read()
    print(content) # This will print the contents of the file
    my_new_file.seek(0) # This will move the cursor to the beginning of the file
    print(my_new_file.readlines()) # This will print the contents of the file as a list of lines

with open('section3/mytextfile.txt', mode='r') as my_new_file:
    content = my_new_file.read()
    print(content) # This will print the contents of the file
    my_new_file.seek(0) # This will move the cursor to the beginning of the file
    print(my_new_file.readlines()) # This will print the contents of the file as a list of lines

with open('section3/mytextfile.txt', mode='a') as f:
    f.write('\nThis is a new line')
    f.seek(0) # This will move the cursor to the beginning of the file

print(content) # This will print the contents of the file

with open('section3/myfilenew.txt', mode='w') as f:
    f.write('This is a new file')
    f.seek(0) # This will move the cursor to the beginning of the file

with open('section3/myfilenew.txt', mode='r') as f:
    print(f.read()) # This will print the contents of the file

with open('thisisanotherfile.txt', mode='w') as f:
    f.write('This is another file')
    f.seek(0) # This will move the cursor to the beginning of the file

with open('thisisanotherfile.txt', mode='r') as f:
    print(f.read()) # This will print the contents of the file