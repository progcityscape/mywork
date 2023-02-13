# This program reads in a string and strips
# any leading or trailing spaces.
# It also converts all the letters to lower case.
# It then outputs the lengths of the original string and the normalised one
# author: John Kelleher

raw_string = input ("Please enter a string: ")
normalised_string = raw_string.strip().lower()

length_raw_string = len(raw_string)
length_norm_string = len(normalised_string)

print(f'That string normalised is: {normalised_string}')
print(f'We reduced the input string from {length_raw_string} to {length_norm_string} characters.')
