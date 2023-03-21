# 10 random numbers between 20000 and 80000
# author: John Kelleher

import numpy as np

# set absolute values
min_salary = 20000
max_salary = 80000
number_of_entries = 10

salaries = np.random.randint(min_salary, max_salary, number_of_entries)
print (salaries)

# the program can be debugged by 'seeding' - ensuring random numbers are same each time

np.random.seed(1)

salaries = np.random.randint(min_salary, max_salary, number_of_entries)
print (salaries)

# make another array of numbers for salaries + 5000
salaries_plus = salaries + 5000
print (salaries_plus)

# increase all salaries by 5%

salaries_mult = salaries * 1.05

# convert into int array
new_salaries = salaries_mult.astype(int)
print (new_salaries)