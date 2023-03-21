# Write a program that makes a list called ages that has, the same number random
# values as salaries (range:21 to 65) . Make scatter plot of this data
# author: John Kelleher

import matplotlib.pyplot as plt
import numpy as np

# set absolute values
min_salary = 20000
max_salary = 80000
number_of_entries = 10
# set absolute values for ages
low = 21
high = 65
size = number_of_entries

# generate random salaries
np.random.seed(1)
salaries = np.random.randint(min_salary, max_salary, number_of_entries)
ages = np.random.randint(low, high, size)

# plot it
plt.scatter(ages, salaries)


# add x squared in a different colour
xpoints = np.array(range(1, 101))
ypoints = xpoints * xpoints 
plt.plot(xpoints, ypoints, color= 'r')


plt.savefig("prettier_plot.png")