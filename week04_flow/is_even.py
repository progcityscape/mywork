# Asks the user to input a number and outputs even or odd.
# Author: John Kelleher

x = 1

# add loop so user is prompted to keep entering integers until they enter -1

while x != -1:

    x = int(input("Enter an integer: "))

    if (x % 2) == 0:
        print (f"{x} is an even number.")
    else:
        print (f"{x} is an odd number.")
