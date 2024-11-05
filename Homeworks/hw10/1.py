import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial

# Actual function
def true_function(x):
    return np.sin(x)

# 6th order Maclaurin polynomial of sin(x)
def maclaurin_sin(x):
    return x - (x**3) / factorial(3) + (x**5) / factorial(5)


# Pade approximation with cubic numerator and denominator
def pade_cubic(x):
    return (x - (7/60)*(x**3)) / (1 + (1/20)*(x**2))

# Pade approximation with quadratic numerator and fourth degree denominator
def pade_quadratic(x):
    return (x) / (1 + (1/6)*(x**2) - (7/360)*(x**4))

# Pade approximation with fourth degree numerator and quadratic numerator
def pade_fourth_order(x):
    return (x - (7/60)*(x**3)) / (1 + (1/20)*(x**2))

# Define the interval
x_values = np.linspace(0, 5, 1000)

# Calculate the true values
true_values = true_function(x_values)

# Calculate the errors for each approximation
error_maclaurin = np.abs(true_values - maclaurin_sin(x_values))
error_pade_cubic = np.abs(true_values - pade_cubic(x_values))
error_pade_quadratic = np.abs(true_values - pade_quadratic(x_values))
error_pade_fourth_order = np.abs(true_values - pade_fourth_order(x_values))

# Plot the errors
plt.figure(figsize=(10, 6))
plt.plot(x_values, error_maclaurin, label='6th Order Maclaurin', color='blue')
plt.plot(x_values, error_pade_cubic, label='Padé (3,3)', color='red')
plt.plot(x_values, error_pade_quadratic, label='Padé (2,4)', color='green')
plt.plot(x_values, error_pade_fourth_order, label='Padé (4,2)', color='purple')

plt.xlabel('x')
plt.xlim(0, 5)  
plt.ylabel('Error')
plt.ylim(0, 12)  
plt.title('Error Comparison of Sin(x) Approximations')
plt.legend()
plt.grid(True)
plt.show()
