# while loop is used to execute a block of statements repeatedly until a given condition is satisfied. And when the condition becomes false, the line immediately after the loop in the program is executed.
# Syntax:
# while condition:
#     statement1
#     statement2
#     ...
# The condition is an expression that evaluates to true or false. If it is true, the statements inside the loop are executed. Otherwise, the loop is terminated.
# Example:
# num = 1
# while num <= 5:
#     print(num)
#     num = num + 1

x = 0 # Change this to 5 to see the other output.
while x < 5:
    print(f'The current value of x is {x}')
    x += 1
else:
    print('x is not less than 5')

x = [1, 2, 3]
for item in x:
    # comment
    pass  # pass is a null statement. It is a placeholder for future code.
print('End of my script')

mystring = 'Sammy'
for letter in mystring:
    if letter == 'a':
        continue
    print(letter) # S m m y

mystring = 'Sammy'
for letter in mystring:
    if letter == 'a':
        break
    print(letter) # S 

x = 0
while x < 5:
    if x == 2:
        break
    print(x)
    x += 1 # 0 1


