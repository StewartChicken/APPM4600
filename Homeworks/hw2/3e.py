import math

# Given value of x
x = 9.999999995000000e-10

f_x = x + ((x**2) / 2)

print("{:.16f}".format(f_x))