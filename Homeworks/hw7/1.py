import numpy as np
import matplotlib.pyplot as plt

# Function to interpolate
def f(x):
    return 1 / (1 + (10 * x)**2)

# Function to generate the Vandermonde matrix
def vandermonde_matrix(x):
    N = len(x)
    return np.vander(x, N, increasing=True)

# Function to find polynomial coefficients using Vandermonde matrix
def polynomial_coefficients(x, y):
    V = vandermonde_matrix(x)
    return np.linalg.solve(V, y)

# Evaluate the polynomial at a given set of points
def evaluate_polynomial(coeffs, x):
    N = len(coeffs)
    return np.polyval(coeffs[::-1], x)

# Parameters
max_N = 20  # Max value of N to observe Runge's phenomenon
x_values = np.linspace(-1, 1, 1001)  # Evaluation points

# Iterate over degrees N
for N in range(2, max_N + 1):
    # Generate interpolation points
    h = 2 / (N - 1)
    x = -1 + (np.arange(1, N + 1) - 1) * h
    y = f(x)
    
    # Find the polynomial coefficients
    coeffs = polynomial_coefficients(x, y)
    
    # Evaluate the polynomial on the fine grid
    p_x = evaluate_polynomial(coeffs, x_values)
    
    # Plot the original function, data points, and polynomial
    plt.figure()
    plt.plot(x_values, f(x_values), label='f(x)', color='blue')
    plt.plot(x, y, 'o', label='Data points', color='red')
    plt.plot(x_values, p_x, label=f'Interpolating Polynomial (N={N})', color='green')
    
    # Add title and labels
    plt.title(f'Interpolation with N={N}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    
    # Show plot
    plt.show()
    
    # Check maximum value of the polynomial
    max_poly_value = np.max(np.abs(p_x))
    if max_poly_value > 100:
        print(f"Runge's phenomenon observed at N={N}, max polynomial value = {max_poly_value}")
        break
