import math

# Given value of x
x = 9.999999995000000e-10

# Algorithm to compute f(x) = e^x - 1
y = math.exp(x)  # Compute e^x
f_x = y - 1      # Subtract 1 to get f(x)

# True value of f(x) is approximately 10^-9
true_value = 1e-9

# Output results
print("{:.16f}".format(f_x))
print("{:.16f}".format(1e-9))
