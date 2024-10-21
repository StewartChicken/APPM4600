import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange, CubicSpline, CubicHermiteSpline

# Function to interpolate
def f(x):
    return 1 / (1 + x**2)

def fp(x):
    return -2*x / ((1 + x**2)**2)

# Define the interval and the number of nodes
interval = [-5, 5]
n_values = [5, 10, 15, 20]
x_plot = np.linspace(interval[0], interval[1], 500)

# Lagrange Interpolation
def lagrange_interpolation(x_nodes, y_nodes):
    poly = lagrange(x_nodes, y_nodes)
    return poly(x_plot)

# Natural Cubic Spline
def natural_cubic_spline(x_nodes, y_nodes):
    spline = CubicSpline(x_nodes, y_nodes, bc_type='natural')
    return spline(x_plot)

# Clamped Cubic Spline (boundary conditions: first derivative at the boundaries = 0)
def clamped_cubic_spline(x_nodes, y_nodes):
    # We can assume that the slope at the boundary is 0 (for clamped condition)
    spline = CubicSpline(x_nodes, y_nodes, bc_type='clamped')
    return spline(x_plot)

# Hermite interpolation using CubicHermiteSpline
def hermite_interpolation(x_nodes, y_nodes, yp_nodes):
    interp = CubicHermiteSpline(x_nodes, y_nodes, yp_nodes)
    return interp(x_plot)

# Compute the average error between an interpolation array and an actual array
def compute_average_error(y_interp, y_actual):
    error = np.abs(y_interp - y_actual)
    return np.mean(error)

# Generates n Chebyshev nodes on the interval [a, b]
def chebyshev_nodes(n, a, b):
    i = np.arange(n)
    nodes = np.cos((2 * i + 1) * np.pi / (2 * n))
    nodes = 0.5 * (nodes + 1) * (b - a) + a  # Scale and shift to interval [a, b]
    return np.sort(nodes)


# Loop over different values of n (number of nodes)
for n in n_values:
    #x_nodes = np.linspace(interval[0], interval[1], n)
    x_nodes = chebyshev_nodes(n, interval[0], interval[1])

    y_nodes = f(x_nodes)
    yp_nodes = fp(x_nodes)

    y_actual = f(x_plot)

    # Plot the original function
    plt.figure(figsize=(10, 6))
    plt.plot(x_plot, y_actual, label="Original function", color='black', linewidth=2)

    # Lagrange
    y_lagrange = lagrange_interpolation(x_nodes, y_nodes)
    plt.plot(x_plot, y_lagrange, '--', label=f'Lagrange n={n}')
    
    # Hermite (simplified with Barycentric)
    y_hermite = hermite_interpolation(x_nodes, y_nodes, yp_nodes)
    plt.plot(x_plot, y_hermite, '-.', label=f'Hermite n={n}')
    
    # Natural cubic spline
    y_natural_spline = natural_cubic_spline(x_nodes, y_nodes)
    plt.plot(x_plot, y_natural_spline, ':', label=f'Natural Cubic Spline n={n}')
    
    # Clamped cubic spline
    y_clamped_spline = clamped_cubic_spline(x_nodes, y_nodes)
    plt.plot(x_plot, y_clamped_spline, '-.', label=f'Clamped Cubic Spline n={n}')

    # Build plot
    plt.legend()
    plt.title("Interpolation Methods on $f(x) = 1 / (1 + x^2)$")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.ylim(-1, 1.5)
    plt.grid(True)
    plt.show()

    # Compute error
    lagrange_avg_error = compute_average_error(y_lagrange, y_actual)
    hermite_avg_error = compute_average_error(y_hermite, y_actual)
    nCubic_avg_error = compute_average_error(y_natural_spline, y_actual)
    cCubic_avg_error = compute_average_error(y_clamped_spline, y_actual)

    print("Lagrange average error: ", lagrange_avg_error)
    print("Hermite average error: ", hermite_avg_error)
    print("Natural Spline average error: ", nCubic_avg_error)
    print("Clamped Spline average error: ", cCubic_avg_error)





