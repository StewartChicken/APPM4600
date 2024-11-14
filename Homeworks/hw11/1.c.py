import numpy as np
from scipy.integrate import quad

# Define the function
def f(s):
    return 1 / (1 + s**2)

# Composite trapezoidal rule
# a, b are the endpoints of the interval
# n is the number of subintervals
def composite_trapezoidal(a, b, n):
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b))

    for i in range(1, n):
        result += f(a + i * h)

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
    result = f(a) + f(b)

    for i in range(1, n, 2):
        result += 4 * f(a + i * h)

    for i in range(2, n - 1, 2):
        result += 2 * f(a + i * h)

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
n_t = 646      # Number of sub-intervals for trapezoidal
n_s = 108      # Number of sub-intervals for Simpson's

# Approximate the integral using both methods
T_n = approximate_integral(a, b, n_t, method="trapezoidal")
S_n = approximate_integral(a, b, n_s, method="simpson")

quad_default, quad_default_err = quad(f, a, b)  # default tolerance is 1e-6
quad_loose, quad_loose_err = quad(f, a, b, epsabs=1e-4)

# Print results and number of function evaluations
print("Results:")
print(f"Composite Trapezoidal Rule (n={n_t}): T_n = {T_n}")
print(f"Composite Simpson's Rule (n={n_s}): S_n = {S_n}")
print(f"SciPy quad (tolerance=1e-6): Result = {quad_default}, Error Estimate = {quad_default_err}")
print(f"SciPy quad (tolerance=1e-4): Result = {quad_loose}, Error Estimate = {quad_loose_err}")

# Report the number of function evaluations
print("\nFunction Evaluations:")
print(f"Trapezoidal Rule requires {n_t + 1} function evaluations")
print(f"Simpson's Rule requires {n_s + 1} function evaluations")
print(f"SciPy quad (tolerance=1e-6) used {quad(f, a, b, full_output=True)[2]['neval']} evaluations")
print(f"SciPy quad (tolerance=1e-4) used {quad(f, a, b, epsabs=1e-4, full_output=True)[2]['neval']} evaluations")