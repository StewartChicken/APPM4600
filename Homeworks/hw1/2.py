import numpy as np
import matplotlib.pyplot as plt

# Define the function to compute the difference between the exact and the expression
def compute_difference(x, delta):
    # Exact difference
    exact_diff = np.cos(x + delta) - np.cos(x)
    # Expression without subtraction
    expr_diff = -2 * np.sin(delta / 2) * np.sin(x + delta / 2)
    # Compute absolute difference
    return np.abs(exact_diff - expr_diff)

# Compute difference between exact and taylor approx
def compute_difference_taylor(x, delta):
    exact_diff = np.cos(x + delta) - np.cos(x)
    taylor_diff = delta*(np.sin(x) - np.sin(x + delta)) + (delta*delta/2)*(np.cos(x)-np.cos(x+delta))

    return np.abs(exact_diff - taylor_diff)

# Compute the difference between approx and taylor approx
def compute_difference_taylor1(x, delta):
    expr_diff = -2 * np.sin(delta / 2) * np.sin(x + delta / 2)
    taylor_diff = delta*(np.sin(x) - np.sin(x + delta)) + (delta*delta/2)*(np.cos(x)-np.cos(x+delta))

    return np.abs(expr_diff - taylor_diff)

# Values of x
x_values = [np.pi, 1e6]

# Values of delta
delta_values = np.logspace(-16, 0, num=50)

# Plot
plt.figure(figsize=(12, 6))

def plot_difference():
    for x in x_values:
        differences = [compute_difference_taylor1(x, delta) for delta in delta_values]
        plt.loglog(delta_values, differences, label=f'x = {x}')

plot_difference()

plt.xlabel('Delta (δ)')
plt.ylabel('Absolute Difference')
plt.title('Difference between Exact and Approximate Cosine Difference')
plt.legend()
plt.grid(True)
plt.show()
