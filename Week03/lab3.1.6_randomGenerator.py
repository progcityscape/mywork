# program prints out a random number between 1 and 10

import random

number = (random.randint(1,10))

print (("Here is a random number: {}").format(number))

# extend to allow user to input randomthe range for the random numbers

x = int(input("Choose your range for the random generator: pick your lowest number: "))
y = int(input("pick your highest number: "))

number = (random.randint(x,y))

print (("Here is a random number: {}").format(number))

