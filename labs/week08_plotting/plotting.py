# plot the function y = x squared
# author: John Kelleher

# import library
import matplotlib.pyplot as plt
import numpy as np


xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints

# plot it
plt.plot (xpoints, ypoints)
# display it
plt.show()
