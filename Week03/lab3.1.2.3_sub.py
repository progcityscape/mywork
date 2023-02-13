# program to subtract one number from another.  Have attempted to include error spotting by using functions.
# author: John Kelleher

def subtract (x,y):
    answer = y-x
    return answer

# some issues with assigning output of function to a variable
# https://stackoverflow.com/questions/35423564/how-can-i-store-a-result-of-a-function-in-a-variable-instead-of-just-printing-it cleared it up

def give_numbers_1 ():
    number1 = (input("Input number to subtract: "))
    return (number1)

def give_numbers_2 ():
    number2 = (input("Input number to subtract from: "))
    return (number2)

# transfer the function outcomes (given numbers) to variables for use in other functions

subtrahend = (give_numbers_1 ())
minuend = (give_numbers_2 ())


def calculate ():
    # check for validity of input numbers
    if subtrahend.isdigit () and minuend.isdigit ():
        subtra_int = int(subtrahend)
        minu_int = int(minuend)
        difference = subtract (subtra_int, minu_int)

        print ("{} minus {} is {} ".format(minuend, subtrahend, difference))
    else:
        print ("Please enter valid numbers next time...")

calculate ()


























