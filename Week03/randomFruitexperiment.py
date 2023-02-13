# this program generates a random fruit

# bring in the module

import random

# make a list

fruits = ['apple', 'orange', 'banana', 'pear']


# loop to remove one item each time until none are left

while len(fruits) >0:

    # we want a random number between 0 and (length -1) 
   
    index = random.randint(0, (len(fruits)-1))

    # get the random fruit using index 
    fruit = fruits[index]
    print ("A Random Fruit is: {}".format(fruit))

    fruits.remove(fruit)
    
   

print ("There are {} items left in the list".format(len(fruits)))






