# take in a float and output an int rounded down
# author: John Kelleher

# built in module
import math

number_to_floor = float(input("Enter a float number: "))
floored_number = math.floor(number_to_floor)
print ("{} floored is {}".format(number_to_floor, floored_number))

