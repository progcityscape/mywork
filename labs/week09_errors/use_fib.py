# prompts the user for a number and prints out the fibonacci sequence for that many numbers
# author: John Kelleher

# bring in module saved in other file
import myfunctions

n_times = int(input("How many?:"))
print (myfunctions.fibonacci(n_times))
