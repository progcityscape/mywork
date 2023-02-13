# read in two numbers and subtract the first from the second.
# author: John Kelleher
# includes experiments with functions

# create a function to reuse in a larger program

def sub_two_numbers(x,y):
    answer = y-x
    print ("The answer is: {}".format(answer))

def input_number_1 ():
    a = (input("Enter the first number: "))
   
    
    # test the number
    if a.isdigit():
        print ("ok")
       

    else:
        print ("no")
     
    

def input_number_2 ():
    b = (input("Enter the number to be subtracted: "))

    # test the number
    if b.isdigit():
        print ("ok")
    
    else:
        print ("no")
    

sub_two_numbers(input_number_1, input_number_2)

print ("Let's do a new subtraction: ")

# check repeatability with new variables

z = int(input("Enter the first number: "))
w = int(input("Enter the number to be subtracted: "))

sub_two_numbers(w,z)





