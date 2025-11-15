import random

x = random.randint(1, 6) # generates random number between 1 and 6
print(x)

y = random.random() # generates random decimal numbers between 0 and 1
print(y)

mylist = ['apple', 'banana', 'cherry']
z = random.choice(mylist) # randomly selects an item from a list
print(z)

cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
random.shuffle(cards) # shuffles the list
print(cards)