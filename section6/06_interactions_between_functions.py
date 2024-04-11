# Tipically a python script or notebook contains several functions interacting with each other
# Let's create a few functions to mimic the carnival guessing game "Three Cup Monte"

# Import library to shuffle
from random import shuffle

# Shuffles the three position list where the "Ball" is placed
def shuffle_list(mylist):
  shuffle(mylist)
  return mylist


# Asks the player in which position considers the ball is placed
def player_guess():
  guess=''
  while guess not in ['0','1','2']:
    guess = input('Pick a number: 0, 1 or 2: ')
  return int(guess)

# Check agains the virtual "Ball" position
def check_guess(mylist,guess):
  if mylist[guess] == 'O':
    print("Correct!")
  else:
    print("Wrong guess!")
    print(mylist)

# Inicial list
mylist = [' ','O',' ']
# Shuffle list
mixedup_list = shuffle_list(mylist)
# User guess
guess = player_guess()
# Check guess
check_guess(mixedup_list,guess)