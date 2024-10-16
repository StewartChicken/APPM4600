import numpy as np
import matplotlib.pyplot as plt

# Function to interpolate
def f(x):
    return 1 / (1 + (10 * x)**2)
    

# Barycentric interpolation function
def barycentric_interpolation(x, x_values, y_values):
    N = len(x_values)
    w = np.zeros(N)

    # Calculate weights
    for j in range(N):
        w[j] = 1 / np.prod(x_values[j] - np.delete(x_values, j))

    # Calculate the interpolation polynomial value
    numerator = np.zeros_like(x)
    denominator = np.zeros_like(x)

    for j in range(N):
        # Evaluate the terms
        term = w[j] / (x - x_values[j])
        numerator += term * y_values[j]
        denominator += term

    return numerator / denominator

# Parameters
max_N = 20  # Max value of N to observe Runge's phenomenon
x_values = np.linspace(-1, 1, 1001)  # Evaluation points

# Iterate over degrees N
for N in range(2, max_N + 1):
    # Generate interpolation points
    h = 2 / (N - 1)
    x = -1 + (np.arange(1, N + 1) - 1) * h
    y = f(x)

    # Perform barycentric interpolation
    p_x = barycentric_interpolation(x_values, x, y)

    # Plot the original function, data points, and polynomial
    plt.figure()
    plt.plot(x_values, f(x_values), label='f(x)', color='blue')
    plt.plot(x, y, 'o', label="Data points", color="red")
    plt.plot(x_values, p_x, label=f'Interpolating Polynomial (N={N})', color='green')

    # Add title and labels
    plt.title(f'Barycentric Lagrange Interpolation with N={N}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    
    # Show plot
    plt.show()



