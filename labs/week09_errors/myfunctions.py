# take a number as input and return that many items in a list of Fibonacci sequence numbers
# author: John Kelleher

# import logging
import logging
# commenting out the following line as it will be included in the file being tested
'''
logging.basicConfig(level = logging.DEBUG)
'''

def fibonacci (number):
    a = 0
    b = 1
    fibonacci_sequence = [0]

    
    for i in range (1, number):
        fibonacci_sequence.append(b)
        a, b = b, a+b
    logging.debug ("%d: %s", number, fibonacci_sequence)       
    
    
    
    if number == 0:
        return []

    if number < 0:
        return ValueError ("Number must be > 0")
    
    return fibonacci_sequence

# testing code
if __name__ == "__main__":
    # tests will go here
    print ("all good")

return7 = [0,1,1,2,3,5,8]
return11 = [0,1,1,2,3,5,8,13,21,34,55]


assert fibonacci(7) == return7, 'incorrect return for 7'
assert fibonacci(11) == return11, 'incorrect return for 11'
assert fibonacci(0) == [], 'incorrect return for 0'
assert fibonacci(1) == [0], 'incorrect return for 1'

'''
try:
    fibonacci(-1)
except ValueError:
    # no need to do anything as we want this value to be thrown
    pass
else:
    assert False, 'fibonacci missing ValueError'

'''