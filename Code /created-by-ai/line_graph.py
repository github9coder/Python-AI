"""You need to import matplotlyb"""

import matplotlib.pyplot as plt
# Data for the x-axis
x = [1, 2, 3, 4, 5]

# Data for the y-axis
y = [10, 15, 13, 18, 16]

# Plotting the line graph
plt.plot(x, y)

# Adding labels to the axes
plt.xlabel('X-axis label')
plt.ylabel('Y-axis label')

# Adding a title to the plot
plt.title('Simple Line Graph')

# Display the plot
plt.show()
