import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
    return x - 4 * np.sin(2 * x) - 3

# Define the range for x
x = np.linspace(-10, 10, 400)
y = f(x)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='f(x) = x - 4 sin(2x) - 3')
plt.axhline(0, color='black',linewidth=0.5)
plt.title('Plot of f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()

# Finding zero crossings
from scipy.optimize import fsolve

def find_zero_crossings(func, x_range):
    zero_crossings = []
    for x in np.linspace(x_range[0], x_range[1], 1000):
        root = fsolve(func, x)
        if np.isclose(func(root), 0, atol=1e-5):
            if root not in zero_crossings:
                zero_crossings.append(root[0])
    return zero_crossings

# Determine the zero crossings within a reasonable range
zero_crossings = find_zero_crossings(f, [-10, 10])

# Plot the zero crossings
for zero in zero_crossings:
    plt.plot(zero, f(zero), 'ro')  # 'ro' for red dots

plt.show()

# Print the number of zero crossings
print(f"Number of zero crossings: {len(zero_crossings)}")
