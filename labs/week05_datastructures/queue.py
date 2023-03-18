# Create a program that puts 10 random numbers into a queue(list), the
# program should then output all the values in the queue, then take the
# numbers from the queue one at a time, print it and the current numbers still
# in the queue. (the command pop(0) takes the first element out of a list)

# author: john kelleher

import random

# generate a random list of numbers
# https://www.geeksforgeeks.org/generating-random-number-list-in-python/

queue =[]
n=10
for i in range(n):
    queue.append(random.randint(0,100))

print (f"queue is {queue}")

while len(queue) != 0:
    # pop(0) removes first element and queue.pop(0) seems to generate jsut the first element for use
    current_number =  queue.pop(0)
    print (f"current number is {current_number} and queue is {queue}")

print ("The queue is now empty")




