import numpy as np

# Define the function
def integrand(s):
    return 1 / (1 + s**2)

# Composite trapezoidal rule
# a, b are the endpoints of the interval
# n is the number of subintervals
def composite_trapezoidal(a, b, n):
    h = (b - a) / n
    result = 0.5 * (integrand(a) + integrand(b))

    for i in range(1, n):
        result += integrand(a + i * h)

    result *= h

    return result

# Composite simpson's rule
# a, b are the endpoints of the interval
# n is the number of subintervals (this must be even)
def composite_simpson(a, b, n):
    # Return zero if odd number of subintervals
    if n % 2 != 0:
        return 0

    h = (b - a) / n
    result = integrand(a) + integrand(b)

    for i in range(1, n, 2):
        result += 4 * integrand(a + i * h)

    for i in range(2, n - 1, 2):
        result += 2 * integrand(a + i * h)

    result *= h / 3
    
    return result

# Based on the method argument, calculates an approximation using either the
# trapezoidal rule or Simpson's rule
def approximate_integral(a, b, n, method="trapezoidal"):
    if method == "trapezoidal":
        return composite_trapezoidal(a, b, n)
    elif method == "simpson":
        return composite_simpson(a, b, n)
    else:
        return 0

# Parameters
a, b = -5, 5  # Interval bounds
n = 20       # Number of sub-intervals

# Approximate the integral using both methods
trapezoidal_result = approximate_integral(a, b, n, method="trapezoidal")
simpson_result = approximate_integral(a, b, n, method="simpson")

# Display the results
print(f"Trapezoidal approximation: {trapezoidal_result}")
print(f"Simpson's approximation: {simpson_result}")
