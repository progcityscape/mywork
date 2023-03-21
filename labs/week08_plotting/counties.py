# Write program that has a list of counties - make a pie chart of the counties
# author: john kelleher

import numpy as np
import matplotlib.pyplot as plt

# make the array of occurences
possible_counties = ['Mayo', 'Galway', 'Roscommon', 'Dublin', 'Donegal']
# pick 100 randomly from counties with freq set in p
counties = np.random.choice(
    possible_counties, p = [0.1, 0.3, 0.2, 0.12, 0.28],
    size = (100)
)

# now return a tuple of unique values and how many times they occur

unique, counts = np.unique(counties, return_counts=True )

'''
# make a pie plot
plt.pie(counts, labels=unique)

plt.show()
'''
plt.bar(unique, counts)
plt.show()