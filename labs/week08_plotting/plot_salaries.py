# make a histogram to plot the salaries from salaries.py
# author: John Kelleher

import matplotlib.pyplot as plt
import numpy as np


# set absolute values
min_salary = 20000
max_salary = 80000
number_of_entries = 10

# the program can be debugged by 'seeding' - ensuring random numbers are same each time

np.random.seed(1)
salaries = np.random.randint(min_salary, max_salary, number_of_entries)


plt.hist(salaries)
plt.show()
