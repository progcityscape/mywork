# read in two numbers and divides the first by the second.
# author: John Kelleher

dividend = int(input("Enter the first number: "))
divisor = int(input("Enter the number you want to divide by: "))

quotient = int(dividend//divisor) # // gives the int division
remainder = int(dividend%divisor) # % for the remainder

print (("{} divided by {} is {} with remainder {}").format(dividend, divisor, quotient, remainder))













