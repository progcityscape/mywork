# Write a program that counts how many times it was run.
# firstly Write a function that reads in a number from a file that already exists
# (count.txt). test the program by calling the function and outputting the
# number.

FILENAME = "count.txt"

# add try/except to the read_number function in case the file does not exist on user's setup

def read_number ():
    try:
        with open (FILENAME) as f:
            number = int(f.read())
            return number
    except IOError:
        # file will be created when we write back
        # no file assumes first time running
        # ie 0 previous runs
        return 0


# test
# num = read_number ()
# print (num)

# Write a function that takes in a number and overwrites a file with that
# number (count.txt).

def write_number (number):
    with open (FILENAME, "wt") as f:
        # write takes a string so convert
        f.write(str(number))

# test

# write_number (3)

# main
num = read_number ()
num += 1

print (f"We have run this program {num} times")

write_number (num)

