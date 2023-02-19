# read in a student's percentage and output corresponding grade
# author: John Kelleher

def enter_percent ():
    percentage = float(input("Enter the percentage: "))
    # modify code to deal with rounding issue e.g. 69.5 should equal distinction
    round_percent = round(percentage)
    return (round_percent)


def output_grade (x):
    # check for error
    if x < 0 or x > 100:
        print("Please enter a number between 0 and 100: ")
    elif x < 40:
        print("Fail")
    elif x < 50:
        print("Pass")
    elif x < 60:
        print("Merit1")
    elif x < 70:
        print("Merit2")
    else:
        print("Distinction")

    
# exploring how concise the code can be for two functions - can I do a function of a function e.g. "var = function1(function2)"
# https://realpython.com/python-return-statement/#:~:text=In%20general%2C%20a%20function%20takes,value%2C%20either%20explicit%20or%20implicit.
# https://www.pythonmorsels.com/passing-functions-arguments-other-functions/#:~:text=In%20Python%20you%20can%20pass%20function%20objects%20in%20to%20other,can%20then%20call%20them%20later.


result = enter_percent()
output_grade(result)





