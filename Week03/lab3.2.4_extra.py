# take in a float amount of dollars and convert to an absolute amount of cents
# author: John Kelleher

# there may be a minus sign in the input

def make_absolute (x):
    absolute_value = abs(x)
    return absolute_value

# using function to convert to cents

def convert_tocents (x):
    # using * to establish cent amount
    cent_amount = int(x*100)
    return cent_amount

float_amount = float(input("What is your float amount of dollars: $"))

cent_amount = convert_tocents(float_amount)
absolute_cents = make_absolute(cent_amount)


print ("Final amount is {} cents.".format(absolute_cents))

# quicker way without functions

float_amount = float(input("What is your float amount of dollars: $"))

cent_amount = int(100*abs(float_amount))

print ("Final amount is {} cents.".format(cent_amount))




    