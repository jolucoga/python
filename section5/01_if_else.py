# If statement in Python
# If statement is used to check a condition: if the condition is true, we run a block of statements (called the if-block), else we process another block of statements (called the else-block). The else clause is optional.
# Syntax:
# if condition:
#     statement1
#     statement2
#     ...
# else:
#     statement3
#     statement4
#     ...
# The condition is an expression that evaluates to true or false. If it is true, the statements in the if-block are executed. Otherwise, the statements in the else-block are executed.
# Example:
# age = 20
# if age >= 18:
#     print('You are an adult.')
# else:
#     print('You are a teenager.')
# Output:
# You are an adult.
# In this example, the condition age >= 18 is true, so the statements in the if-block are executed. The else-block is skipped.
# Note: The indentation is very important in Python. The statements in the if-block and else-block must be indented with the same number of spaces. The standard indentation is 4 spaces.

if True:
    print('This is true.') # This is true.
else:
    print('This is false.') # This is false.

hungry = False  # Change this to True to see the other output.
if hungry:
    print('I am hungry.') # I am hungry.
else:
    print('I am not hungry.') # I am not hungry.

loc = 'Bank'  # Change this to 'Store' to see the other output. 
if loc == 'Auto Shop':
    print('Cars are cool!')
elif loc == 'Bank':
    print('Money is cool!') # Money is cool!
elif loc == 'Store':
    print('Welcome to the store!')
else:
    print('I do not know much.')

name = 'Sammy'  # Change this to 'Frankie' to see the other output.
if name == 'Frankie':
    print('Hello Frankie!')
elif name == 'Sammy':
    print('Hello Sammy!') # Hello Sammy!
else:
    print('What is your name?')


  