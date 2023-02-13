# read in two numbers and subtract the first from the second.
# author: John Kelleher
# includes experiments with functions

# create a function to reuse in a larger program

def sub_two_numbers(x,y):
    answer = y-x
    print ("The answer is: {}".format(answer))

def input_numbers ():
    y = int(input("Enter the first number: "))
    x = int(input("Enter the number to be subtracted: "))
    return x,y
    print (x,y)


input_numbers ()

print ("Let's do a new subtraction: ")

# check repeatability with new variables

z = int(input("Enter the first number: "))
w = int(input("Enter the number to be subtracted: "))

sub_two_numbers(w,z)





